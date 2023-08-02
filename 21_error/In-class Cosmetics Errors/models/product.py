from models.gender import Gender

class Product:
    def __init__(self, name: str, brand: str, price: float, gender: Gender):
        self.name = name
        self.brand = brand
        self.price = price
        self._gender = gender


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            if len(value) >= 3 or len(value) <= 10:
                self._name = value
        except ValueError:
            print('Name should be between 3 and 10 symbols.')
            

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        try:
            if len(value) >= 2 or len(value) <= 10:
                self._brand = value
        except ValueError:
            print('Brand should be between 2 and 10 symbols.')


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            if value > 0:
                self._price = value
        except ValueError as error:
            print('Price should not be negative.', error)



    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        try:
            if value in ['Men', 'Women', 'Unisex']:
                self._gender = value    
        except Exception:
            print("The gender can be Men', 'Women' or 'Unisex'")


    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender.value}',
            ' ==='
        ])
    


# Validations
# Name should be between 3 and 10 symbols.      da
# Name should be unique in the system.           da
# Brand should be between 2 and 10 symbols.    da
# Price cannot be negative.                       da
# Gender type can be "Men", "Women" or "Unisex".  da
