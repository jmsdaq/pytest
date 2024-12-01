import pytest
from app.shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item("Laptop", 1000, 2)
    assert cart.items["Laptop"]["quantity"] == 2

def test_remove_item(cart):
    cart.add_item("Laptop", 1000, 2)
    cart.remove_item("Laptop", 1)
    assert cart.items["Laptop"]["quantity"] == 1

def test_apply_coupon(cart):
    cart.add_item("Laptop", 1000, 1)
    cart.apply_coupon(10)
    assert cart.get_total_price() == 900

def test_clear_cart(cart):
    cart.add_item("Laptop", 1000, 1)
    cart.clear_cart()
    assert len(cart.items) == 0
