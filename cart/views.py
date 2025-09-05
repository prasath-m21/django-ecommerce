# cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    """
    Add a product to the cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        
        # Check if requested quantity is available
        current_cart_item = cart.get_item(product)
        current_quantity = current_cart_item['quantity'] if current_cart_item else 0
        
        if cd['update']:
            # Updating quantity
            if cd['quantity'] > product.stock:
                messages.error(request, f'Sorry, only {product.stock} items available.')
                return redirect('cart:cart_detail')
        else:
            # Adding to existing quantity
            total_quantity = current_quantity + cd['quantity']
            if total_quantity > product.stock:
                available = product.stock - current_quantity
                messages.error(
                    request, 
                    f'Sorry, you can only add {available} more items. '
                    f'You already have {current_quantity} in your cart.'
                )
                return redirect('store:product_detail', slug=product.slug)
        
        # Add to cart
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
        
        messages.success(request, f'{product.name} added to cart!')
    
    # Redirect to cart page or previous page
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """
    Remove a product from cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f'{product.name} removed from cart.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    """
    Display the cart and its contents.
    """
    cart = Cart(request)
    
    # Add update forms to each item
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            }
        )
    
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_clear(request):
    """
    Clear all items from the cart.
    """
    cart = Cart(request)
    cart.clear()
    messages.info(request, 'Your cart has been cleared.')
    return redirect('store:home')
