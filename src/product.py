```python
class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a new product instance.

        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product in stock
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        """
        Calculate the total value of the product in stock.

        :return: Total value of the product in stock
        """
        return self.price * self.quantity

    def restock(self, amount):
        """
        Add more stock to the product.

        :param amount: Amount to add to the current stock
        """
        self.quantity += amount

    def sell(self, amount):
        """
        Sell a certain amount of the product.

        :param amount: Amount to sell
        :raises ValueError: If the amount to sell is greater than the quantity in stock
        """
        if amount > self.quantity:
            raise ValueError("Not enough stock to sell")
        self.quantity -= amount

    def __str__(self):
        """
        Return a string representation of the product.

        :return: String representation of the product
        """
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
```