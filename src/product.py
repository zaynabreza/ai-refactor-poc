import sqlite3

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, percent):
        return self.price - (self.price * percent / 100)

def get_product_by_name(user_input):
conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    query = "SELECT * FROM products WHERE name = ?"
    cursor.execute(query, (user_input,))
    return cursor.fetchall()

def get_products_cheaper_than(max_price):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM products WHERE price < {max_price}"
    cursor.execute(query)
    return cursor.fetchall()

