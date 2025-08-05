from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from apps.products.models import Product
from .cart import Cart
import json


def cart_detail(request):
    """Display cart contents"""
    cart = Cart(request)
    
    # Check stock availability for each item
    for item in cart:
        product = item['product']
        if product.track_inventory and item['quantity'] > product.stock_quantity:
            # Adjust quantity if stock changed
            cart.update_quantity(product.id, product.stock_quantity)
            messages.warning(
                request, 
                f'Quantity for {product.name} adjusted to available stock.'
            )
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    """Add product to cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Get quantity from form
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1
    
    # Check if product is in stock
    if not product.is_in_stock:
        messages.error(request, f'{product.name} is out of stock.')
        return redirect('products:product_detail', slug=product.slug)
    
    # Check quantity against stock
    if product.track_inventory:
        current_in_cart = 0
        cart_item = cart.get_item(product_id)
        if cart_item:
            current_in_cart = cart_item['quantity']
        
        if current_in_cart + quantity > product.stock_quantity:
            available = product.stock_quantity - current_in_cart
            if available > 0:
                messages.warning(
                    request, 
                    f'Only {available} more {product.name} available.'
                )
                quantity = available
            else:
                messages.error(
                    request, 
                    f'Cannot add more {product.name}. Maximum quantity in cart.'
                )
                return redirect('products:product_detail', slug=product.slug)
    
    # Add to cart
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'{product.name} added to cart.')
    
    # Return JSON response for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'message': f'{product.name} added to cart.',
            'cart_count': len(cart),
            'cart_total': round(float(cart.get_total_price()), 2)
        })
    
    # Redirect to cart or back to product
    next_url = request.POST.get('next', 'cart:cart_detail')
    return redirect(next_url)


@require_POST
def cart_update(request):
    """Update cart quantities"""
    cart = Cart(request)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            
            if product_id and quantity >= 0:
                if quantity == 0:
                    # Remove item
                    product = get_object_or_404(Product, id=product_id)
                    cart.remove(product)
                    message = 'Item removed from cart.'
                    item_total = 0
                else:
                    # Update quantity
                    success = cart.update_quantity(product_id, quantity)
                    if success:
                        message = 'Cart updated.'
                        # Calculate item total
                        item = cart.get_item(product_id)
                        item_total = 0
                        if item:
                            item_total = float(item['price']) * item['quantity']
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Error updating cart.'})
                
                return JsonResponse({
                    'status': 'success',
                    'message': message,
                    'cart_count': len(cart),
                    'cart_total': float(cart.get_total_price()),
                    'item_total': float(item_total)
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid product ID or quantity'})
        except (ValueError, TypeError):
            return JsonResponse({'status': 'error', 'message': 'Invalid quantity'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'An error occurred'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def cart_remove(request, product_id):
    """Remove product from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)
    messages.success(request, f'{product.name} removed from cart.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'message': 'Item removed from cart.',
            'cart_count': len(cart),
            'cart_total': float(cart.get_total_price())
        })
    
    return redirect('cart:cart_detail')


def cart_clear(request):
    """Clear all items from cart"""
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Cart cleared.')
    
    return redirect('products:product_list')