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
