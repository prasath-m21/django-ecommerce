# store/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Product, Category
from cart.forms import CartAddProductForm


def home(request):
    """
    Home page view displaying all products with optional search.
    """
    # Get search query from request
    search_query = request.GET.get('q', '')
    
    # Get all available products
    products = Product.objects.filter(available=True)
    
    # Apply search filter if query exists
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Get all categories for the dropdown menu
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'total_products': products.count(),
    }
    
    return render(request, 'store/home.html', context)


def about(request):
    """
    About page view with company information.
    """
    # Get all categories for the dropdown menu
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
    }
    
    return render(request, 'store/about.html', context)


def product_detail(request, slug):
    """
    Product detail view showing individual product information.
    """
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    # Add cart form
    cart_product_form = CartAddProductForm()
    
    context = {
        'product': product,
        'related_products': related_products,
        'cart_product_form': cart_product_form,
    }
    
    return render(request, 'store/product_detail.html', context)