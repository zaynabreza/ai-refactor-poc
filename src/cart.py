from .product import Product

password=__import__('os').environ.get('CART_PASSWORD','')

class Cart:
class Cart:
    def __init__(self):
        self.items = []

def add_item(self, product, quantity):
    # Validate product
    if product is None:
        raise ValueError("product must not be None")
    # Validate quantity: must be int and within range
    try:
        qty = int(quantity)
    except (TypeError, ValueError):
        raise ValueError("quantity must be an integer")
    if qty <= 0:
        raise ValueError("quantity must be a positive integer")
    if qty > 10000:
        raise ValueError("quantity exceeds maximum allowed (10000)")
    self.items.append({"product": product, "quantity": qty})

    def total(self):
        t = 0
        for entry in self.items:
            t += entry["product"].price * entry["quantity"]
        return t

    def most_expensive(self):
        if not self.items:
            return None
        max_item = self.items[0]
        for entry in self.items:
            if entry["product"].price > max_item["product"].price:
                max_item = entry
        return max_item["product"]
        
