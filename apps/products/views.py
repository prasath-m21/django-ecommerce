from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Avg
from .models import Product, Category, Tag, ProductReview


def product_list_view(request):
    """Display all products with filtering and pagination"""
    products = Product.objects.filter(is_active=True).select_related('category')
    
    # Search
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Tag filter
    tag_slug = request.GET.get('tag')
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags=tag)
    
    # Price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Sorting
    sort = request.GET.get('sort', '-created_at')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    elif sort == 'rating':
        products = products.order_by('-rating_average')
    else:
        products = products.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(products, 12)  # 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for sidebar
    categories = Category.objects.filter(is_active=True, parent=None)
    
    context = {
        'page_obj': page_obj,
        'products': page_obj,
        'categories': categories,
        'current_query': query,
        'current_sort': sort,
    }
    
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, slug):
    """Display single product details"""
    product = get_object_or_404(
        Product.objects.select_related('category').prefetch_related('images', 'tags'),
        slug=slug,
        is_active=True
    )
    
    # Increment view count
    product.view_count += 1
    product.save(update_fields=['view_count'])
    
    # Get reviews
    reviews = product.reviews.filter(is_approved=True).select_related('user')
    
    # Get related products
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    # Check if user can review
    can_review = False
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        # In real app, check if user purchased this product
        can_review = not user_review
    
    context = {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'can_review': can_review,
        'user_review': user_review,
    }
    
    return render(request, 'products/product_detail.html', context)


def category_view(request, slug):
    """Display products in a specific category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(
        category=category,
        is_active=True
    ).select_related('category')
    
    # Apply same filtering as product list
    # ... (similar code as product_list_view)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'products': page_obj,
    }
    
    return render(request, 'products/category.html', context)
