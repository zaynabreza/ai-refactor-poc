```python
import unittest
from cart import Cart, Item

class TestCart(unittest.TestCase):
    def setUp(self):
        """Set up a Cart instance for testing."""
        self.cart = Cart()

    def test_add_item(self):
        """Test adding an item to the cart."""
        item = Item('apple', 1.0)
        self.cart.add_item(item)
        self.assertIn(item, self.cart.items)

    def test_remove_item(self):
        """Test removing an item from the cart."""
        item = Item('apple', 1.0)
        self.cart.add_item(item)
        self.cart.remove_item(item)
        self.assertNotIn(item, self.cart.items)

    def test_total_price(self):
        """Test calculating the total price of items in the cart."""
        item1 = Item('apple', 1.0)
        item2 = Item('banana', 2.0)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.total_price(), 3.0)

    def test_clear_cart(self):
        """Test clearing all items from the cart."""
        item = Item('apple', 1.0)
        self.cart.add_item(item)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.items), 0)

    def test_item_quantity(self):
        """Test updating the quantity of an item in the cart."""
        item = Item('apple', 1.0, quantity=2)
        self.cart.add_item(item)
        self.assertEqual(self.cart.items[0].quantity, 2)

    def test_update_item_quantity(self):
        """Test updating the quantity of an existing item in the cart."""
        item = Item('apple', 1.0, quantity=2)
        self.cart.add_item(item)
        self.cart.update_item_quantity(item, 5)
        self.assertEqual(self.cart.items[0].quantity, 5)

    def test_item_not_in_cart(self):
        """Test removing an item not in the cart."""
        item = Item('apple', 1.0)
        with self.assertRaises(ValueError):
            self.cart.remove_item(item)

    def test_update_quantity_item_not_in_cart(self):
        """Test updating the quantity of an item not in the cart."""
        item = Item('apple', 1.0)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity(item, 5)

if __name__ == '__main__':
    unittest.main()
```