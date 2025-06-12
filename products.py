class Product:
    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity


    def get_quantity(self):
        """Return the quantity of the product."""
        return self.quantity


    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        self.quantity = quantity


    def is_active(self):
        """Return True if the product is active, False otherwise."""
        return self.quantity > 0


    def active(self):
        """Sets the product to active"""
        return self.is_active()


    def deactivate(self):
        """Sets the product to inactive"""
        self.quantity = 0


    def show(self):
        """Return a string showing the product."""
        return f"{self.name}, Price: {self.price},  Quantity{self.quantity}"


    def buy(self, quantity):
        """Buys the product, recalculates the stock and calculates the total price."""
        if quantity > self.quantity:
            print("Not enough quantity in stock!")
        self.quantity -= quantity
        return self.price * quantity



