class Category:
    def __init__(self, name):
        self._name = name
        self._products_in_category = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Illegal description length (2:15 char)')
        if type(value) != str:
            raise ValueError("Must be string")
        self._name = value

    @property   # products property getter should return an immutable collection (tuple)
    def products(self):
        for el in self._products_in_category:
            return tuple(el)

    def add_product(self, new_product_name):
        self._products_in_category.append(new_product_name)

    def remove_product(self, product_to_remove):
        if product_to_remove not in self._products_in_category:
            raise ValueError("404: The product you want to remove is not found")

    def to_string(self):
        raise NotImplementedError()
