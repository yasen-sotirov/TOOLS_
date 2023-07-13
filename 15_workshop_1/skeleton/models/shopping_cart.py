class ShoppingCart:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return ShoppingCart.products

    def add_product(self, product):
       self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    def contains_product(self, product):
        return self._products

    def total_price(self):
        total_price = 0
        for current_product in self._products:
            total_price += current_product.price
        return total_price



