class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.quantity > 0

    def active(self):
        return self.is_active()

    def deactive(self):
        self.quantity = 0

    def show(self):
        return f"{self.name}, Price: {self.price},  Quantity{self.quantity}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock!")
        self.quantity -= quantity
        return self.price * quantity

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == '__main__':
    main()


