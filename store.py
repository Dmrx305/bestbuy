class Store:
    def __init__(self,product_list):
        """Initialize the store."""
        self.products = product_list


    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self):
        """Return the total quantity of the product."""
        return sum(product.quantity for product in self.products if product.is_active())


    def get_all_products(self):
        """Return all the products in the store that are active"""
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        """Buys all the products on the shopping list."""
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
