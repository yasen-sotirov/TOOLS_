from models.product import Product


class Toothpaste(Product):
    def __init__(self, name, brand, price: float, gender, *ingredients):
        super().__init__(name, brand, price, gender)
        self.ingredients = ingredients

    def to_string(self):
        return f"{Product.to_string(self)}\n #Ingredients: [{', '.join(self.ingredients)}]"


tooth_1 = Toothpaste("White", "Expensive", 10.99, "Men",  "calcium, fluorid")
print(tooth_1.to_string())