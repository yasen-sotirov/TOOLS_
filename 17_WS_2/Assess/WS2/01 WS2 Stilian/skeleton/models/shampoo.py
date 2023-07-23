from models.product import Product
from models.usage_type import UsageType


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        super().__init__(name, brand, price, gender)
        self.usage_type = usage_type
        self.milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value):
        if value < 0:
            raise ValueError("Milliliters can't be less than zero!")
        self._milliliters = value

    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        self._usage_type = UsageType.from_string(value)

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Milliliters: {self._milliliters}',
            f' #Usage: {self._usage_type}'
        ])
