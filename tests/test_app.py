import pytest
from app import app
from app.models import User, Product

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_data():
    # Reset in-memory data between tests
    global users, products
    users = {}
    products = {}
    return users, products

def test_add_user(client):
    response = client.post('/user', json={"username": "john_doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert b"User john_doe added." in response.data

def test_add_product(client):
    response = client.post('/product', json={"name": "Laptop", "price": 1000.00, "stock": 10})
    assert response.status_code == 200
    assert b"Product Laptop added." in response.data

def test_add_to_cart(client):
    client.post('/product', json={"name": "Laptop", "price": 1000.00, "stock": 10})
    response = client.post('/cart', json={"item_name": "Laptop", "quantity": 2})
    assert response.status_code == 200
    assert b"2 x Laptop added to cart." in response.data

def test_checkout(client):
    client.post('/product', json={"name": "Laptop", "price": 1000.00, "stock": 10})
    client.post('/cart', json={"item_name": "Laptop", "quantity": 2})
    response = client.post('/cart/checkout', json={"username": "john_doe"})
    assert response.status_code == 200
    assert b"Order placed successfully." in response.data
    assert b"total" in response.data
