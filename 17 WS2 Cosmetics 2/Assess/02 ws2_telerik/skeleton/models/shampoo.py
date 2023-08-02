from models.product import Product

class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        super().__init__(name, brand, price, gender)
        self._usage_type = usage_type
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value):
        if value < 0:
            raise ValueError('Milliliters cannot be negative.')
        self._milliliters = value

    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        self._usage_type = value

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Milliliters: {self.milliliters}',
            f' #Usage Type: {self.usage_type}'
        ])
