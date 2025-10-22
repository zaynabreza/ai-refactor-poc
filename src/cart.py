```python
class Cart:
    def __init__(self):
        """Initialize an empty cart."""
        self.items = []

    def add_item(self, item, quantity):
        """Add an item to the cart.

        Args:
            item (str): The name of the item.
            quantity (int): The quantity of the item.
        """
        self.items.append({'item': item, 'quantity': quantity})

    def remove_item(self, item):
        """Remove an item from the cart.

        Args:
            item (str): The name of the item to remove.
        """
        self.items = [i for i in self.items if i['item'] != item]

    def get_total_items(self):
        """Get the total number of items in the cart.

        Returns:
            int: The total number of items.
        """
        return sum(item['quantity'] for item in self.items)

    def get_items(self):
        """Get a list of items in the cart.

        Returns:
            list: A list of items in the cart.
        """
        return self.items

    def clear_cart(self):
        """Clear all items from the cart."""
        self.items = []

    def __str__(self):
        """Return a string representation of the cart.

        Returns:
            str: A string representation of the cart.
        """
        return f"Cart({self.items})"
```