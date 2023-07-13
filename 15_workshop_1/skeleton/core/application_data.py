import models.product
from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        # self.ShopingCart

    @property
    def products(self):
        return models.product.Product.all_products

    @property
    def categories(self):
        return models.category.Category.all_categories

    @property
    def shopping_cart(self) -> ShoppingCart:
        raise NotImplementedError()

    def find_product_by_name(self, name) -> Product:
        for obj in models.product.Product.all_products:
            if name == obj:
                return obj
        raise ValueError(f"404: The product {name} can't be found.")

    def find_category_by_name(self, name) -> Category:
        for obj in models.category.Category.all_categories:
            if name == obj:
                return models.category.Category.all_categories[name]
        raise ValueError(f"404: The category {name} can't be found.")

    def create_category(self, name) -> None:
        if len(models.category.Category.all_categories) > 0:
            for el in models.category.Category.all_categories:
                if el.name == name:
                    raise ValueError(f"The category with name {name} already exist.")
        models.category.Category.name.setter(name)

    def create_product(self, name, brand, price, gender) -> None:
        # би трябвало да създаден нов обект със зададените аргументи
        models.product.Product(name, brand, price, gender)

    def category_exists(self, name) -> bool:
        for obj in models.category.Category.all_categories:
            if name == obj:
                return True
            raise False

    def product_exists(self, name) -> bool:
        for obj in models.product.Product.all_products:
            if name == obj.name:
                return True
            return False
