# store/admin.py

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Category model.
    """
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Product model.
    """
    list_display = ['name', 'category', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'category', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['category']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    # Custom admin actions
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        """
        Admin action to mark selected products as available.
        """
        updated = queryset.update(available=True)
        self.message_user(request, f'{updated} products marked as available.')
    make_available.short_description = "Mark selected products as available"
    
    def make_unavailable(self, request, queryset):
        """
        Admin action to mark selected products as unavailable.
        """
        updated = queryset.update(available=False)
        self.message_user(request, f'{updated} products marked as unavailable.')
    make_unavailable.short_description = "Mark selected products as unavailable"
