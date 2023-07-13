class Product:
    all_products = []

    def __init__(self, name: str, brand: str, price: float, gender: str):
        if len(name) < 3 or len(name) > 10:
            raise ValueError('Illegal product name. The name length must be 3-10 char')
        if len(brand) < 2 or len(brand) > 10:
            raise ValueError('Illegal brand name. The name length must be 2-10 char')
        if price < 0:
            raise ValueError("The product price can't be negative number")

        self._name = name
        self._brand = brand
        self._price = price
        # в отделен файл проверява зададения пол
        self._gender = gender
        # добавя новосъздадения обект към листа на класа
        Product.all_products.append(self)

# име на продукта
    @property       # връща името на продукта по сигурен начин
    def name(self) -> str:
        return self._name

    @name.setter    # проверява името и го задава
    def name(self, value: str):
        if len(value) < 3 or len(value) > 10:
            raise ValueError('Illegal product name. The name length must be 3-10 char')
        self._name = value

# име на бранда
    @property       # връща името по сигурен начин
    def brand(self) -> str:
        return self._brand

    @brand.setter       # проверява името и го задава
    def brand(self, value: str):
        if len(value) < 2 or len(value) > 10:
            raise ValueError('Illegal brand name. The name length must be 2-10 char')
        self._brand = value

# цена на продукта
    @property       # връща стойността на цената по сигурен начин
    def price(self) -> float:
        return self._price

    @price.setter       # проверява цената да е на +
    def price(self, value: float):
        if value < 0:
            raise ValueError("The product price can't be negative number")
        self._price = value

    @property       # връща зададения пол
    def gender(self):
        return self._gender

# връща стринг репрезентация
    def to_string(self):
        result = f""" #{self.name} {self.brand}
 #Price: ${self.price:.02f}
 #Gender: {self.gender}"""
        return result
