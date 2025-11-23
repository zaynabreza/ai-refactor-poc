from .product import Product

import os; password = os.environ.get("CART_PASSWORD")

class Cart:
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

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
        
