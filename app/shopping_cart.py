class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.coupons = []

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=None):
        if item_name in self.items:
            if quantity is None or self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def apply_coupon(self, discount_percentage):
        self.coupons.append(discount_percentage)

    def get_total_price(self):
        total = sum(details['price'] * details['quantity'] for details in self.items.values())
        for coupon in self.coupons:
            total *= (1 - coupon / 100)
        return round(total, 2)

    def clear_cart(self):
        self.items = {}
        self.coupons = []
