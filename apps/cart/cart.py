from decimal import Decimal
from django.conf import settings
from apps.products.models import Product


class Cart:
    """
    Shopping cart class to manage cart operations
    """
    
    def __init__(self, request):
        """Initialize the cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            # Create empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to cart or update its quantity
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'name': product.name,
                'slug': product.slug,
                'sku': product.sku,
            }
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        # Ensure quantity doesn't exceed stock
        if product.track_inventory:
            if self.cart[product_id]['quantity'] > product.stock_quantity:
                self.cart[product_id]['quantity'] = product.stock_quantity
        
        self.save()
    
    def save(self):
        """Mark session as modified to save it"""
        self.session.modified = True
    
    def remove(self, product):
        """Remove a product from cart"""
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """Iterate over cart items and fetch products from database"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        # Create a dict to map product IDs to products
        products_dict = {str(product.id): product for product in products}
        
        for product_id, item in self.cart.items():
            # Get the product from our dict (don't store it in session)
            product = products_dict.get(product_id)
            if product:  # Only yield if product still exists
                yield {
                    'product': product,
                    'price': Decimal(item['price']),
                    'quantity': item['quantity'],
                    'total_price': Decimal(item['price']) * item['quantity']
                }
    
    def __len__(self):
        """Count all items in cart"""
        return sum(item['quantity'] for item in self.cart.values())
    
    def __bool__(self):
        """Return True if cart has items"""
        return bool(self.cart)
    
    def get_total_price(self):
        """Calculate total price of all items"""
        return sum(
            Decimal(item['price']) * item['quantity'] 
            for item in self.cart.values()
        )
    
    def clear(self):
        """Remove cart from session"""
        if settings.CART_SESSION_ID in self.session:
            del self.session[settings.CART_SESSION_ID]
            self.save()
    
    def get_item(self, product_id):
        """Get specific item from cart"""
        return self.cart.get(str(product_id))
    
    def update_quantity(self, product_id, quantity):
        """Update quantity for a specific product"""
        product_id = str(product_id)
        
        if product_id in self.cart:
            if quantity <= 0:
                # Remove item if quantity is 0 or negative
                del self.cart[product_id]
                self.save()
                return True
            else:
                # Get product to check stock
                try:
                    product = Product.objects.get(id=product_id)
                    if product.track_inventory and quantity > product.stock_quantity:
                        quantity = product.stock_quantity
                    
                    self.cart[product_id]['quantity'] = quantity
                    self.save()
                    return True
                except Product.DoesNotExist:
                    # Remove item if product no longer exists
                    del self.cart[product_id]
                    self.save()
                    return False
        
        return False