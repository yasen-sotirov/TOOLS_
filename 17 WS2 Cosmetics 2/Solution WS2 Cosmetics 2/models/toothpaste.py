from models.product import Product


class Toothpaste(Product):
    def __init__(self, name, brand, price, gender, ingredients):
        super().__init__(name, brand, price, gender)
        self._ingredients = ingredients

    @property
    def ingredients(self):
        return tuple(self._ingredients)

    def to_string(self):
        formatted_ingredients = f' #Ingredients: [{", ".join(self._ingredients)}]'

        return f'{super().to_string()}\n{formatted_ingredients}'

    