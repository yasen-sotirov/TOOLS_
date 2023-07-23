from models.product import Product


class Toothpaste(Product):
    def __init__(self, name, brand, price, gender, ingredients):
        super().__init__(name, brand, price, gender)

        self._ingredients = ingredients

    @property
    def ingredients(self):
        return tuple(self._ingredients)
    
    @ingredients.setter
    def ingredients(self, value):
        self.ingr = ''
        self.ingr += value
        self._ingredients = self.ingr

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Ingredients: [{self._ingredients}]'
        ])