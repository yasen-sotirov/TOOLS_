from models.product import Product


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
            raise ValueError('Milliliters should not be negative.')

        self._milliliters = value

    # @property
    # def usage_type(self):
    #     return self._usage_type

    def to_string(self):
        return f'{super().to_string()}\n #Milliliters: {self._milliliters}\n #Usage: {self.usage_type}'
