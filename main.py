import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    while True:
        print("\nStore Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4 .Quit")

        try:
            customer_choice = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if customer_choice == 1:
            for product in best_buy.products:
                print(f"{product.name}, Price: {product.price},  Quantity: {product.quantity}")

        elif customer_choice == 2:
            print(f"Total of {best_buy.get_total_quantity()} items in store")

        elif customer_choice == 3:
            shopping_list = []
            print("\nEnter the product you want to buy and the according quantity")
            print("When you're finished, hit Enter to continue")
            print()
            all_products = best_buy.get_all_products()

            for i, product in enumerate(best_buy.products, start =1):
                print(f"{i}.{product.name}, Price: {product.price},  Quantity: {product.quantity}")
            print()
            while True:
                try:
                    product_choice = input("Please choose a number(1-3): ")

                    if product_choice == "":
                        break
                    product_index = int(product_choice)
                    if product_index not in range(1, len(all_products) + 1):
                        print("Invalid input. Please enter a valid product number.")
                        continue

                    quantity = int(input("Please choose quantity: "))
                    shopping_list.append((all_products[int(product_choice)-1], quantity))
                    if quantity > all_products[product_index - 1].quantity:
                        print("not enough stock available!")
                        continue

                except ValueError:
                    print("Invalid input. Please enter only numbers.")

            total_price = best_buy.order(shopping_list)
            print(f"\nOrder made, total price: ${total_price}")

        elif customer_choice == 4:
            break


def main():
    start()


if __name__ == "__main__":
    main()