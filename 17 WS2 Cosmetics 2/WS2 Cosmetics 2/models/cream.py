from models.product import Product
from models.scent import Scent


class Cream(Product):

    def __init__(self, name, brand, price, gender, scent):
        super().__init__(name, brand, price, gender)
        self.scent = scent

    @property
    def scent(self):
        return self.scent

    @scent.setter
    def scent(self, value):
        if Scent.from_string(value):
            self.scent = value

    def to_string(self):
        return f"{Product.to_string(self)}\n #Scent: {self.scent}"
