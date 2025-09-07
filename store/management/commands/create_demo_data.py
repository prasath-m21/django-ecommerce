from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = "Refresh demo categories and products"

    def handle(self, *args, **kwargs):
        # Clear old demo data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        electronics = Category.objects.create(
            name="Electronics",
            description="Electronic gadgets"
        )
        clothing = Category.objects.create(
            name="Clothing",
            description="Fashion items"
        )

        # Add all products (same as before)
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
            image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="Powerbank",
            slug="powerbank",
            description="Portable 20000mAh powerbank",
            category=electronics,
            price="49.99",
            stock=40,
            image_url="https://images.unsplash.com/photo-1594843665794-446ce915d840?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="Earpods",
            slug="earpods",
            description="True wireless earbuds",
            category=electronics,
            price="89.99",
            stock=35,
            image_url="https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="Jeans",
            slug="jeans",
            description="Comfortable denim jeans",
            category=clothing,
            price="59.99",
            stock=20,
            image_url="https://plus.unsplash.com/premium_photo-1674828601362-afb73c907ebe?q=80&w=453&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="T-Shirt",
            slug="t-shirt",
            description="Casual cotton t-shirt",
            category=clothing,
            price="19.99",
            stock=100,
            image_url="https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="Bag",
            slug="bag",
            description="Premium Quality Bag",
            category=clothing,
            price="39.99",
            stock=15,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?q=80&w=438&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        Product.objects.create(
            name="Blazer",
            slug="blazer",
            description="Formal men's blazer",
            category=clothing,
            price="129.99",
            stock=12,
            image_url="https://images.unsplash.com/photo-1598808503746-f34c53b9323e?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        self.stdout.write(self.style.SUCCESS("✅ Demo data refreshed successfully!"))
