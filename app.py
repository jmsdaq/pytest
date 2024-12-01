# app.py

from flask import Flask, request, jsonify
from app.models import User, Product, Order
from app.shopping_cart import ShoppingCart

app = Flask(__name__)

users = {}
products = {}
cart = ShoppingCart()

@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    email = data['email']
    users[username] = User(username, email)
    return jsonify({"message": f"User {username} added."})

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    price = data['price']
    stock = data['stock']
    products[name] = Product(name, price, stock)
    return jsonify({"message": f"Product {name} added."})

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    item_name = data['item_name']
    quantity = data['quantity']
    product = products.get(item_name)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    if product.stock < quantity:
        return jsonify({"error": "Not enough stock"}), 400
    cart.add_item(item_name, product.price, quantity)
    return jsonify({"message": f"{quantity} x {item_name} added to cart."})

@app.route('/cart/checkout', methods=['POST'])
def checkout():
    username = request.json['username']
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    order = Order(user)
    for item_name, details in cart.items.items():
        product = products[item_name]
        quantity = details['quantity']
        order.add_item(product, quantity)
        product.reduce_stock(quantity)
    user.place_order(order)
    cart.clear_cart()
    return jsonify({"message": "Order placed successfully.", "total": order.total})

if __name__ == '__main__':
    app.run(debug=True)
