# store/models.py

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import os

class Category(models.Model):
    """
    Product category model to organize products.
    Examples: Electronics, Clothing, Books, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """
        Meta options for the Category model.
        """
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']  # Sort categories by name
    
    def __str__(self):
        """
        String representation of the category.
        This is what will show in the admin panel and shell.
        """
        return self.name

class Product(models.Model):
    """
    Product model representing items in our store.
    """
    # Basic product information
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    
    # Relationships
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    # Pricing and inventory
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    
    # Image fields
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('store:product_detail', args=[self.slug])
    
    @property
    def is_in_stock(self):
        return self.stock > 0 and self.available
    
    def get_image_url(self):
        """Get product image URL - either uploaded image or external URL"""
        if self.image:
            return self.image.url
        return self.image_url or 'https://via.placeholder.com/300x300?text=No+Image'

    """
    Product model representing items in our store.
    """
    # Basic product information
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    
    # Relationships
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    # Pricing and inventory
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    
    # Image fields
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('store:product_detail', args=[self.slug])
    
    @property
    def is_in_stock(self):
        return self.stock > 0 and self.available
    
    def get_image_url(self):
        """Get product image URL - either uploaded image or external URL"""
        if self.image:
            return self.image.url
        return self.image_url or 'https://via.placeholder.com/300x300?text=No+Image'

    """
    Product model representing items in our store.
    """
    # Basic product information
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    
    # Relationships
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    # Pricing and inventory
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    
    # Image will be added later when we configure media files
    # For now, we'll use a placeholder
    image_url = models.URLField(max_length=500, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """
        Meta options for the Product model.
        """
        ordering = ['-created_at']  # Newest products first
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        """
        String representation of the product.
        """
        return self.name
    
    def get_absolute_url(self):
        """
        Returns the URL to access a particular product instance.
        We'll implement this in the URLs step.
        """
        from django.urls import reverse
        return reverse('store:product_detail', args=[self.slug])
    
    @property
    def is_in_stock(self):
        """
        Check if the product is in stock.
        Returns True if stock > 0 and product is available.
        """
        return self.stock > 0 and self.available
