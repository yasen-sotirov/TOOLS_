from models.product import Product

class Toothpaste(Product):
    def __init__(self, name, brand, price, gender, ingredients):
        super().__init__(name, brand, price, gender)
        self._ingredients = ingredients

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, str):
            raise ValueError('Ingredients should be a string.')
        self._ingredients = value

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Ingredients: {self.ingredients}',
        ])