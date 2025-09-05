# store/management/commands/add_more_products.py
from django.core.management.base import BaseCommand
from store.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Adds more products to the database'

    def handle(self, *args, **kwargs):
        # Get or create categories
        electronics = Category.objects.get_or_create(name="Electronics")[0]
        clothing = Category.objects.get_or_create(name="Clothing")[0]
        books = Category.objects.get_or_create(name="Books")[0]
        home = Category.objects.get_or_create(name="Home & Garden")[0]
        sports = Category.objects.get_or_create(name="Sports & Outdoors")[0]
        
        # Additional products data
        new_products = [
            # Electronics
            {
                "name": "Wireless Earbuds Pro",
                "slug": "wireless-earbuds-pro",
                "description": "Premium noise-cancelling wireless earbuds with 30-hour battery life",
                "category": electronics,
                "price": Decimal("149.99"),
                "stock": 45,
                "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400"
            },
            {
                "name": "Smart Watch Ultra",
                "slug": "smart-watch-ultra",
                "description": "Advanced fitness tracking and health monitoring smartwatch",
                "category": electronics,
                "price": Decimal("399.99"),
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"
            },
            {
                "name": "Tablet Pro 12.9",
                "slug": "tablet-pro-129",
                "description": "Professional-grade tablet with stylus support",
                "category": electronics,
                "price": Decimal("899.99"),
                "stock": 15,
                "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"
            },
            # Clothing
            {
                "name": "Premium Leather Jacket",
                "slug": "premium-leather-jacket",
                "description": "Genuine leather jacket with modern fit",
                "category": clothing,
                "price": Decimal("299.99"),
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400"
            },
            {
                "name": "Designer Sunglasses",
                "slug": "designer-sunglasses",
                "description": "UV protection polarized designer sunglasses",
                "category": clothing,
                "price": Decimal("179.99"),
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400"
            },
            # Home & Garden
            {
                "name": "Smart Air Purifier",
                "slug": "smart-air-purifier",
                "description": "HEPA filter air purifier with app control",
                "category": home,
                "price": Decimal("249.99"),
                "stock": 18,
                "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400"
            },
            {
                "name": "Indoor Plant Collection",
                "slug": "indoor-plant-collection",
                "description": "Set of 5 easy-care indoor plants with pots",
                "category": home,
                "price": Decimal("89.99"),
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400"
            },
            # Sports
            {
                "name": "Yoga Mat Premium",
                "slug": "yoga-mat-premium",
                "description": "Extra thick non-slip yoga mat with carrying strap",
                "category": sports,
                "price": Decimal("49.99"),
                "stock": 50,
                "image_url": "https://images.unsplash.com/photo-1592432678016-e910b452f9a2?w=400"
            },
            {
                "name": "Camping Tent 4-Person",
                "slug": "camping-tent-4person",
                "description": "Waterproof family camping tent with easy setup",
                "category": sports,
                "price": Decimal("199.99"),
                "stock": 12,
                "image_url": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=400"
            },
            # Books
            {
                "name": "Django for Professionals",
                "slug": "django-for-professionals",
                "description": "Advanced web development with Django framework",
                "category": books,
                "price": Decimal("44.99"),
                "stock": 40,
                "image_url": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400"
            }
        ]
        
        # Create products
        for product_data in new_products:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f"Created: {product.name}")
            else:
                self.stdout.write(f"Already exists: {product.name}")
        
        self.stdout.write(self.style.SUCCESS(f"\nTotal products in database: {Product.objects.count()}"))
