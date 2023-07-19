from models.product import Product


class Toothpaste(Product):
    def __init__(self, name, brand, price: float, gender, *ingredients):
        super().__init__(name, brand, price, gender)
        self.ingredients = ingredients

    @property
    def ingredients(self):
        return tuple(self._ingredients)

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

        # self.ingredients = ingredients[0]
        # self.igr = self.ingredients.split(',')
    #
    # @property
    # def ingredient(self):
    #     return self._ingredients

    def to_string(self):
        return f"{Product.to_string(self)}\n #Ingredients: [{', '.join(self.ingredients)}]"
