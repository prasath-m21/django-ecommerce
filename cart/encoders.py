# cart/encoders.py

import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles Decimal types"""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)
