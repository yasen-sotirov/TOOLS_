from models.product import Product


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        
        super().__init__(name, brand, price, gender)

        self._validate_mililiters(milliliters)

        self._usage_type = usage_type
        self._milliliters = milliliters

    @property
    def usage_type(self):
        return self._usage_type
    
    @usage_type.setter
    def usage_type(self, value):
        self._validate_usage_(value)
        self._usage_type = value

    @property
    def milliliters(self):
        return self._milliliters
    
    @milliliters.setter
    def milliliters(self, value):
        self._validate_mililiters(value)
        self._milliliters = value

    def _validate_usage_(self, value):
        from usage_type import UsageType
        UsageType.from_string(value)

    def _validate_mililiters(self, mililiters):
        if mililiters < 0:
            raise ValueError('Mililiters can not be negative!')
        
    def to_string(self):
        return '\n' .join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Milliliters: {self._milliliters:.0f}',
            f' #Usage: {self._usage_type}'
        ])
        



