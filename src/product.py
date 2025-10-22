class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, percent):
        return self.price - (self.price * percent / 100)