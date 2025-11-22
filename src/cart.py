from .product import Product


import os

password = os.getenv("CART_PASSWORD")
if not password:
    raise RuntimeError("CART_PASSWORD environment variable is required and must not be empty.")

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
        