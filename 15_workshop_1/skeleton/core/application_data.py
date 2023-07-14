import models.product
from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:

    def __init__(self):
        self._products: list[Product] = []
        self._categories: list = []
        self._shopping_cart = ShoppingCart()

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name) -> Product:
        for obj in self.products:
            if name == obj.name:
                return obj
        raise ValueError(f"404: The product {name} can't be found.")

    def find_category_by_name(self, name) -> Category:
        for obj in self.categories:
            if name == obj.name:
                return obj
        raise ValueError(f"404: The category {name} can't be found.")

    def create_category(self, name) -> None:
        if len(self.categories) > 0:
            for el in self.categories:
                if el.name == name:
                    raise ValueError(f"The category with name {name} already exist.")
        self._categories.append(Category(name))

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            raise ValueError("The product exist")
        self._products.append(Product(name, brand, price, gender))

    def category_exists(self, name) -> bool:
        # for obj in self.categories:
        #     if name == obj.name:
        #         return True
        # return False
        return any(category.name == name for category in self.categories)

    def product_exists(self, name) -> bool:
        for obj in self.products:
            if name == obj.name:
                return True
        return False
