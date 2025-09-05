# store/management/commands/update_product_images.py
from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Updates all existing products with proper image URLs'

    def handle(self, *args, **kwargs):
        # Products with their image URLs
        product_images = {
            'gaming-laptop': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400',
            'wireless-mouse': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400',
            '4k-monitor': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400',
            'smartphone': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400',
            'cotton-t-shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400',
            'denim-jeans': 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=400',
            'running-shoes': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400',
            'python-programming': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400',
            'web-dev-guide': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400',
            'coffee-maker': 'https://images.unsplash.com/photo-1570824104453-508955ab713e?w=400',
            'garden-tools': 'https://images.unsplash.com/photo-1461354464878-ad92f492a5a0?w=400',
            'wireless-earbuds-pro': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400',
            'smart-watch-ultra': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400',
            'tablet-pro-129': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400',
            'premium-leather-jacket': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
            'designer-sunglasses': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400',
            'smart-air-purifier': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
            'indoor-plant-collection': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400',
            'yoga-mat-premium': 'https://images.unsplash.com/photo-1592432678016-e910b452f9a2?w=400',
            'camping-tent-4person': 'https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=400',
            'django-for-professionals': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400',
            'python-programming-book': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400',
            'web-development-guide': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400',
            'garden-tools-set': 'https://images.unsplash.com/photo-1461354464878-ad92f492a5a0?w=400',
        }
        
        # Update products that don't have images
        products_updated = 0
        products_without_images = Product.objects.filter(image_url='') | Product.objects.filter(image_url__isnull=True)
        
        for product in products_without_images:
            if product.slug in product_images:
                product.image_url = product_images[product.slug]
                product.save()
                products_updated += 1
                self.stdout.write(f'Updated image for: {product.name}')
            else:
                # Default image for products not in the list
                product.image_url = 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'
                product.save()
                products_updated += 1
                self.stdout.write(f'Added default image for: {product.name}')
        
        # Also update any placeholder images
        placeholder_products = Product.objects.filter(image_url__contains='placeholder')
        for product in placeholder_products:
            if product.slug in product_images:
                product.image_url = product_images[product.slug]
                product.save()
                products_updated += 1
                self.stdout.write(f'Replaced placeholder for: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully updated {products_updated} product images'
            )
        )
