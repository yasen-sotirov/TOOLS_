class Category:

    def __init__(self, name):
        if len(name) < 2 or len(name) > 15:
            raise ValueError('Illegal description length (2:15 char)')

        self._name = name
        self._products_in_category = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Illegal description length (2:15 char)')
        self._name = value

    @property
    def products(self):
        return tuple(self._products_in_category)

    def add_product(self, product):
        if product in self._products_in_category:
            raise ValueError(f"The product {product} is already added")
        self._products_in_category.append(product)

    def remove_product(self, product):
        if product not in self._products_in_category:
            error = f'''#Category: {self._name}
 #No products in this category'''
            raise ValueError(error)
        self._products_in_category.remove(product)

    def to_string(self):
        category_as_string = f"#Category: {self.name} \n"
        for current_product in self.products:
            category_as_string += current_product.to_string()
        category_as_string += '\n ===\n'
        return category_as_string
