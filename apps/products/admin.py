from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Tag, Product, ProductImage, ProductReview


class ProductImageInline(admin.TabularInline):
    """Inline admin for product images"""
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_main', 'order']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for categories"""
    list_display = ['name', 'parent', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'parent', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'parent')
        }),
        ('Details', {
            'fields': ('description', 'image', 'is_active')
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin configuration for tags"""
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for products"""
    list_display = [
        'name', 'category', 'price_display', 'stock_status', 
        'is_active', 'is_featured', 'rating_display', 'created_at'
    ]
    list_filter = [
        'is_active', 'is_featured', 'category', 
        'tags', 'created_at', 'track_inventory'
    ]
    search_fields = ['name', 'description', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['tags']
    readonly_fields = [
        'view_count', 'sold_count', 'rating_average', 
        'rating_count', 'created_at', 'updated_at'
    ]
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name', 'slug', 'sku', 'category', 'tags'
            )
        }),
        ('Descriptions', {
            'fields': (
                'short_description', 'description'
            )
        }),
        ('Pricing', {
            'fields': (
                'price', 'compare_price'
            )
        }),
        ('Inventory', {
            'fields': (
                'stock_quantity', 'track_inventory', 'weight'
            )
        }),
        ('Visibility', {
            'fields': (
                'is_active', 'is_featured'
            )
        }),
        ('SEO', {
            'fields': (
                'meta_title', 'meta_description'
            ),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': (
                'view_count', 'sold_count', 'rating_average', 
                'rating_count', 'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )
    
    def price_display(self, obj):
        """Display price with currency"""
        if obj.compare_price:
            return format_html(
                '<s style="color: #999;">${}</s> <strong>${}</strong>',
                obj.compare_price, obj.price
            )
        return f"${obj.price}"
    price_display.short_description = 'Price'
    
    def stock_status(self, obj):
        """Display stock status with color"""
        if not obj.track_inventory:
            return format_html('<span style="color: blue;">Not tracked</span>')
        elif obj.stock_quantity > 10:
            color = 'green'
            status = f'In stock ({obj.stock_quantity})'
        elif obj.stock_quantity > 0:
            color = 'orange'
            status = f'Low stock ({obj.stock_quantity})'
        else:
            color = 'red'
            status = 'Out of stock'
        
        return format_html(
            '<span style="color: {};">{}</span>',
            color, status
        )
    stock_status.short_description = 'Stock'
    
    def rating_display(self, obj):
        """Display rating with stars"""
        if obj.rating_count == 0:
            return "No ratings"
        stars = '★' * int(obj.rating_average)
        return f"{stars} {obj.rating_average:.1f} ({obj.rating_count})"
    rating_display.short_description = 'Rating'


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    """Admin configuration for reviews"""
    list_display = [
        'product', 'user', 'rating_stars', 'title', 
        'is_verified_purchase', 'is_approved', 'created_at'
    ]
    list_filter = [
        'rating', 'is_verified_purchase', 'is_approved', 'created_at'
    ]
    search_fields = ['product__name', 'user__email', 'title', 'comment']
    readonly_fields = ['product', 'user', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Review Information', {
            'fields': (
                'product', 'user', 'rating', 'title', 'comment'
            )
        }),
        ('Status', {
            'fields': (
                'is_verified_purchase', 'is_approved'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )
    
    def rating_stars(self, obj):
        """Display rating as stars"""
        return '★' * obj.rating
    rating_stars.short_description = 'Rating'
