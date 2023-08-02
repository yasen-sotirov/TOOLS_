from models.product import Product


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        super().__init__(name, brand, price, gender)
        self.usage_type = usage_type
        self.milliliters = milliliters

    @property
    def usage(self) -> str:
        return self.usage_type

    @usage.setter
    def usage(self, value: str):
        if not value == "Every_Day" or not value == "Medical":
            raise ValueError("The usage_type must be Every_Day or Medical")
        self.usage_type = value

    @property
    def milliliters(self) -> int:
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value: int):
        if int(value) < 0:
            raise ValueError("The milliliters must be positive number")
        self._milliliters = value

    def to_string(self):
        return f"{Product.to_string(self)}\n #Milliliters: {self.milliliters}\n #Usage: {self.usage}"
