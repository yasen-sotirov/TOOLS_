"CLASSMETHOD & STATICMETHOD"    #

# Основната цел на клас методите е да създават инстанция с предефинирани атрибути
# Обикновена функция вложена в класа чисто по организационни причини - не ползва достъп до класа или инстанциите му

class Pizza:
    def __init__(self, name: str, price: float, order: int, ingredients: list):
        self.name = name
        self.price = price
        self.order = order
        self.ingredients = ingredients


    @classmethod                # метод на класа. Работи с класа като цяло
    def peperoni(cls, order):
        ingredients = ['salami', 'mozzarella']
        return cls('Peperoni', 20, order, ingredients)

    @classmethod
    def quattro_formaggi(cls, order):
        ingredients = ['camenber', 'brie', 'gauda', 'emental']
        return cls('Quattro formaggi', 19, order, ingredients)


    def __str__(self):
        return (f'order: {self.order} \n'
                f'name: {self.name} \n'
                f'price: {self.price} \n'
                f'ingredients: {", ".join(self.ingredients)}\n'
                f'====================')


    @staticmethod
    def get_order(order):
        order = int(order)
        return order




pizza_1 = Pizza.quattro_formaggi(1001)
pizza_2 = Pizza.quattro_formaggi(1002)
print(pizza_1)
print()
print(pizza_2)


