"""
Script to create sample products for testing
Run with: python manage.py shell < create_sample_products.py
"""

from apps.products.models import Category, Tag, Product, ProductImage
from decimal import Decimal
import random

# Delete existing data
print("Cleaning existing data...")
Product.objects.all().delete()
Category.objects.all().delete()
Tag.objects.all().delete()

# Create categories
print("Creating categories...")
electronics = Category.objects.create(
    name="Electronics",
    description="Electronic devices and accessories"
)

clothing = Category.objects.create(
    name="Clothing",
    description="Fashion and apparel"
)

books = Category.objects.create(
    name="Books",
    description="Books and reading materials"
)

home = Category.objects.create(
    name="Home & Garden",
    description="Home improvement and garden supplies"
)

# Create subcategories
laptops = Category.objects.create(
    name="Laptops",
    parent=electronics,
    description="Laptop computers"
)

phones = Category.objects.create(
    name="Smartphones",
    parent=electronics,
    description="Mobile phones"
)

# Create tags
print("Creating tags...")
tags = []
tag_names = ["New Arrival", "Best Seller", "On Sale", "Premium", "Eco-Friendly", "Limited Edition"]
for tag_name in tag_names:
    tag = Tag.objects.create(name=tag_name)
    tags.append(tag)

# Create products
print("Creating products...")

# Electronics products
products_data = [
    {
        "name": "Premium Laptop Pro 15",
        "category": laptops,
        "price": 1299.99,
        "compare_price": 1499.99,
        "description": "High-performance laptop with 15-inch display, Intel Core i7 processor, 16GB RAM, and 512GB SSD. Perfect for professionals and content creators.",
        "short_description": "Powerful 15-inch laptop for professionals",
        "stock_quantity": 15,
        "sku": "LAP-PRO-15"
    },
    {
        "name": "Smartphone X Pro Max",
        "category": phones,
        "price": 999.99,
        "compare_price": 1199.99,
        "description": "Latest flagship smartphone with 6.7-inch OLED display, triple camera system, 5G connectivity, and all-day battery life.",
        "short_description": "Flagship smartphone with pro camera",
        "stock_quantity": 25,
        "sku": "PHONE-X-MAX"
    },
    {
        "name": "Wireless Noise-Canceling Headphones",
        "category": electronics,
        "price": 249.99,
        "compare_price": 299.99,
        "description": "Premium wireless headphones with active noise cancellation, 30-hour battery life, and superior sound quality.",
        "short_description": "Premium ANC wireless headphones",
        "stock_quantity": 50,
        "sku": "HEAD-WL-ANC"
    },
    {
        "name": "4K Webcam Pro",
        "category": electronics,
        "price": 149.99,
        "description": "Professional 4K webcam with auto-focus, built-in microphone, and wide-angle lens. Ideal for video conferencing and streaming.",
        "short_description": "4K webcam for professionals",
        "stock_quantity": 30,
        "sku": "CAM-4K-PRO"
    },
    {
        "name": "Designer T-Shirt Premium Cotton",
        "category": clothing,
        "price": 39.99,
        "compare_price": 49.99,
        "description": "Premium 100% cotton t-shirt with modern fit and designer graphics. Available in multiple colors and sizes.",
        "short_description": "Premium cotton designer t-shirt",
        "stock_quantity": 100,
        "sku": "TSH-PREM-01"
    },
    {
        "name": "Classic Denim Jeans",
        "category": clothing,
        "price": 79.99,
        "description": "Classic fit denim jeans made from high-quality denim. Comfortable and durable for everyday wear.",
        "short_description": "Classic fit denim jeans",
        "stock_quantity": 75,
        "sku": "JEAN-CLS-01"
    },
    {
        "name": "Python Programming Masterclass",
        "category": books,
        "price": 49.99,
        "compare_price": 59.99,
        "description": "Comprehensive guide to Python programming from beginner to advanced. Includes practical examples and projects.",
        "short_description": "Complete Python programming guide",
        "stock_quantity": 40,
        "sku": "BOOK-PY-01"
    },
    {
        "name": "Smart Garden Kit",
        "category": home,
        "price": 89.99,
        "description": "Indoor smart garden kit with LED grow lights, automatic watering system, and smartphone app control.",
        "short_description": "Smart indoor gardening system",
        "stock_quantity": 20,
        "sku": "GARD-SMT-01"
    },
]

created_products = []
for data in products_data:
    product = Product.objects.create(**data)
    
    # Add random tags
    random_tags = random.sample(tags, random.randint(1, 3))
    product.tags.set(random_tags)
    
    # Set featured for some products
    if random.choice([True, False]):
        product.is_featured = True
        product.save()
    
    # Set random ratings
    product.rating_average = Decimal(str(random.uniform(3.5, 5.0)))
    product.rating_count = random.randint(5, 100)
    product.save()
    
    created_products.append(product)
    print(f"Created product: {product.name}")

print(f"\nSuccessfully created {len(created_products)} products!")
print("\nCategories created:")
for cat in Category.objects.all():
    print(f"- {cat.name} ({cat.products.count()} products)")

print("\nYou can now visit /products/ to see the product listing!")
