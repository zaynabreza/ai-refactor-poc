
from src.cart import Cart
from src.product import Product

def test_cart_total():
    cart = Cart()
    cart.add_item(Product("Apple", 1), 3)
    cart.add_item(Product("Banana", 2), 2)
    assert cart.total() == 7

def test_most_expensive():
    cart = Cart()
    p1 = Product("Apple", 1)
    p2 = Product("Banana", 2)
    cart.add_item(p1, 1)
    cart.add_item(p2, 1)
    assert cart.most_expensive() == p2
