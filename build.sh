#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create demo data using shell commands
python manage.py shell << EOF
from store.models import Category, Product

if not Category.objects.exists():
    # Create categories
    electronics = Category.objects.create(name="Electronics", description="Electronic gadgets")
    clothing = Category.objects.create(name="Clothing", description="Fashion items")
    
    # Create products
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
    
    print("Demo data created successfully!")
EOF
