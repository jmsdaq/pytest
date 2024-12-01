from app import app
from flask import request, jsonify
from app.models import User, Product  # Corrected import path
from app.shopping_cart import ShoppingCart  # Corrected import path

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
    order = {"user": username, "items": cart.items, "total": cart.get_total_price()}
    user.place_order(order)
    cart.clear_cart()
    return jsonify({"message": "Order placed successfully.", "total": order["total"]})
