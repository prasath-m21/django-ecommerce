# store/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Populates the database with sample categories and products'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create categories
        self.stdout.write('Creating categories...')
        categories_data = [
            ("Electronics", "Electronic gadgets and devices"),
            ("Clothing", "Fashion and apparel"),
            ("Books", "Physical and digital books"),
            ("Home & Garden", "Everything for your home"),
            ("Sports & Outdoors", "Sports equipment and outdoor gear"),
        ]
        
        categories = {}
        for name, description in categories_data:
            category = Category.objects.create(
                name=name,
                description=description
            )
            categories[name] = category
            self.stdout.write(f'Created category: {name}')
        
        # Create products
        self.stdout.write('Creating products...')
        products_data = [
            # Electronics
            ("Gaming Laptop", "gaming-laptop", "High-performance laptop for gaming", "Electronics", 1299.99, 15),
            ("Wireless Mouse", "wireless-mouse", "Ergonomic wireless mouse", "Electronics", 39.99, 50),
            ("4K Monitor", "4k-monitor", "Ultra HD 4K display monitor", "Electronics", 449.99, 20),
            ("Smartphone", "smartphone", "Latest model smartphone", "Electronics", 799.99, 30),
            
            # Clothing
            ("Cotton T-Shirt", "cotton-t-shirt", "100% cotton comfortable t-shirt", "Clothing", 19.99, 100),
            ("Denim Jeans", "denim-jeans", "Classic blue denim jeans", "Clothing", 59.99, 75),
            ("Running Shoes", "running-shoes", "Professional running shoes", "Clothing", 89.99, 40),
            
            # Books
            ("Python Programming", "python-programming", "Learn Python from scratch", "Books", 34.99, 25),
            ("Web Development Guide", "web-dev-guide", "Complete guide to web development", "Books", 29.99, 30),
            
            # Home & Garden
            ("Coffee Maker", "coffee-maker", "Automatic coffee maker", "Home & Garden", 79.99, 20),
            ("Garden Tools Set", "garden-tools", "Complete gardening tools set", "Home & Garden", 49.99, 15),
        ]
        
        for name, slug, description, category_name, price, stock in products_data:
            Product.objects.create(
                name=name,
                slug=slug,
                description=description,
                category=categories[category_name],
                price=price,
                stock=stock,
                image_url=f"https://via.placeholder.com/300x300?text={name.replace(' ', '+')}"
            )
            self.stdout.write(f'Created product: {name}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated database with {Category.objects.count()} categories '
                f'and {Product.objects.count()} products'
            )
        )
