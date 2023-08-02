from models.product import Product
from models.usage_type import UsageType


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        super().__init__(name, brand, price, gender)
        self.milliliters = milliliters
        self.usage_type = usage_type

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value):
        if int(value) < 0:
            raise ValueError("Milliliters cannot be negative.")
        self._milliliters = int(value)

    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        usag = UsageType.from_string(value)
        self._usage_type = usag

    def to_string(self):
        return "\n".join(
            [
                f" #{self.name} {self.brand}",
                f" #Price: ${self.price:.2f}",
                f" #Gender: {self.gender}",
                f" #Milliliters: {self.milliliters}",
                f" #Usage: {self.usage_type}",
            ]
        )
