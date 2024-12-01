# app/models.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= quantity


class Order:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0

    def add_item(self, product, quantity):
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        self.items.append({"product": product, "quantity": quantity})
        self.total += product.price * quantity
