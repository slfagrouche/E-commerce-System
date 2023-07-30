class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def display_cart(self):
        total_cost = 0
        for item in self.cart_items:
            print(f"{item['name']} - ${item['price']}")
            total_cost += item['price']
        print(f"Total: ${total_cost}")
