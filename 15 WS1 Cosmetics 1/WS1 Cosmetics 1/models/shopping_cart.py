class ShoppingCart:
    shopping_carts = []

    def __init__(self):
        self._products = []
        ShoppingCart.shopping_carts.append(self)

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    def contains_product(self, product):
        if product in self._products:
            return True
        return False

    def total_price(self):
        total_price = 0
        for current_product in self._products:
            total_price += current_product.price
        return total_price
