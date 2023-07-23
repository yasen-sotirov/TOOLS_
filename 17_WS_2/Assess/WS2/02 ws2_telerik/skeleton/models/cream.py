from models.product import Product
from models.gender import Gender

class Cream(Product):
    def __init__(self, name, brand, price, gender, scent):
        super().__init__(name, brand, price, gender)
        self._scent = scent

    @property
    def scent(self):
        return self._scent

    # @scent.setter
    # def scent(self, value)
    #     self._scent = value

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Scent: {self.scent}'
        ])