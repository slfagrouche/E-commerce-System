from shopping_cart import ShoppingCart
from products import PRODUCTS

def main():
    cart = ShoppingCart()

    print("Welcome to our Simple E-commerce System!")
    print("Available Products:")
    for product_id, product_info in PRODUCTS.items():
        print(f"{product_id}: {product_info['name']} - ${product_info['price']}")

    while True:
        option = input("Enter product ID to add to cart (or 'checkout' to complete purchase): ")
        if option.lower() == 'checkout':
            print("Your Shopping Cart:")
            cart.display_cart()
            print("Thank you for shopping with us!")
            break
        elif option in PRODUCTS:
            cart.add_to_cart(PRODUCTS[option])
            print(f"{PRODUCTS[option]['name']} added to the cart.")
        else:
            print("Invalid product ID. Please try again.")


main()
