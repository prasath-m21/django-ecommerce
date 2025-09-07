from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = "Create demo categories and products"

    def handle(self, *args, **kwargs):
        if not Category.objects.exists():
            # Create categories
            electronics = Category.objects.create(
                name="Electronics",
                description="Electronic gadgets"
            )
            clothing = Category.objects.create(
                name="Clothing",
                description="Fashion items"
            )

            # Electronics products
            Product.objects.create(
                name="Demo Laptop",
                slug="demo-laptop",
                description="High-performance laptop",
                category=electronics,
                price="999.99",
                stock=10,
                image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"
            )

            Product.objects.create(
                name="Wireless Mouse",
                slug="wireless-mouse",
                description="Ergonomic mouse",
                category=electronics,
                price="29.99",
                stock=50,
                image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400"
            )

            Product.objects.create(
                name="Smartphone",
                slug="smartphone",
                description="Latest model smartphone",
                category=electronics,
                price="699.99",
                stock=30,
                image_url="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"
            )

            Product.objects.create(
                name="Headphones",
                slug="headphones",
                description="Noise-cancelling headphones",
                category=electronics,
                price="149.99",
                stock=25,
                image_url="https://images.unsplash.com/photo-1511367461989-f85a21fda167?w=400"
            )

            Product.objects.create(
                name="Powerbank",
                slug="powerbank",
                description="Portable 20000mAh powerbank",
                category=electronics,
                price="49.99",
                stock=40,
                image_url="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=400"
            )

            Product.objects.create(
                name="Earpods",
                slug="earpods",
                description="True wireless earbuds",
                category=electronics,
                price="89.99",
                stock=35,
                image_url="https://images.unsplash.com/photo-1585386959984-a4155224a1ad?w=400"
            )

            # Clothing products
            Product.objects.create(
                name="Jeans",
                slug="jeans",
                description="Comfortable denim jeans",
                category=clothing,
                price="59.99",
                stock=20,
                image_url="https://images.unsplash.com/photo-1583001593651-6e9a4f7f39e0?w=400"
            )

            Product.objects.create(
                name="T-Shirt",
                slug="t-shirt",
                description="Casual cotton t-shirt",
                category=clothing,
                price="19.99",
                stock=100,
                image_url="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=400"
            )

            Product.objects.create(
                name="Kurta",
                slug="kurta",
                description="Traditional ethnic kurta",
                category=clothing,
                price="39.99",
                stock=15,
                image_url="https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=400"
            )

            Product.objects.create(
                name="Blazer",
                slug="blazer",
                description="Formal men's blazer",
                category=clothing,
                price="129.99",
                stock=12,
                image_url="https://images.unsplash.com/photo-1520975922071-a45c3d74a9b9?w=400"
            )

            self.stdout.write(self.style.SUCCESS("✅ Demo data created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Categories already exist. Skipping demo data."))
