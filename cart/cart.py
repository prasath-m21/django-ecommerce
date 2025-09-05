# cart/cart.py

from decimal import Decimal
from django.conf import settings
from store.models import Product
import json
from .encoders import DecimalEncoder

class Cart:
    """
    A shopping cart class that manages cart operations using sessions.
    """
    
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        self.session_key = settings.CART_SESSION_ID
        
        # Get cart from session or create empty dict
        cart = self.session.get(self.session_key)
        if cart is None:
            cart = self.session[self.session_key] = {}
        
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        
        # Always store price as string to avoid serialization issues
        price_str = str(product.price)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': price_str
            }
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
    
    def save(self):
        """
        Mark the session as modified to make sure it gets saved.
        """
        # Ensure all prices are strings before saving
        for product_id in self.cart:
            if isinstance(self.cart[product_id].get('price'), Decimal):
                self.cart[product_id]['price'] = str(self.cart[product_id]['price'])
        
        self.session[self.session_key] = self.cart
        self.session.modified = True
    
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_dict = {str(p.id): p for p in products}
        
        for product_id, item_data in self.cart.items():
            product = products_dict.get(product_id)
            if product:
                # Create a copy of item data
                item = item_data.copy()
                item['product'] = product
                # Convert string price back to Decimal for calculations
                item['price'] = Decimal(item_data['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        total = Decimal('0.00')
        for item in self.cart.values():
            price = Decimal(str(item['price']))
            total += price * item['quantity']
        return total
    
    def clear(self):
        """
        Remove cart from session.
        """
        self.cart = {}
        self.session[self.session_key] = {}
        self.session.modified = True
    
    def get_item(self, product):
        """
        Get a specific item from the cart.
        """
        product_id = str(product.id)
        return self.cart.get(product_id)
