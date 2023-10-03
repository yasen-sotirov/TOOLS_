from models.product import Product


class Category:
    def __init__(self, name: str):
        self.name = name
        self._products: list[Product] = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Name should be between 2 and 15 symbols.')
        self._name = value
            

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product: Product):    # продукта същ в категорията или същ. по принцип
        try:
            if Category.product_exist_in_category:
                self._products.append(product)
        except Exception:
            print("The product already exist")



    def remove_product(self, product: Product):
        try:
            if Category.product_exist_in_category:
                self._products.remove(product)
        
        except ValueError:
            print("The product doesn't exist")
        
   

    def product_exist_in_category(self, name):
        return name in [p.name for p in self._products]



    def to_string(self):
        new_line = '\n'
        if len(self._products) > 0:
            product_strings = [p.to_string() for p in self._products]
            return f'#Category: {self.name}{new_line}{new_line.join(product_strings)}'
        else:
            return f'#Category: {self.name}{new_line} #No products in this category'



# Name should be between 3 and 10 symbols.  da
# Name should be unique in the system.