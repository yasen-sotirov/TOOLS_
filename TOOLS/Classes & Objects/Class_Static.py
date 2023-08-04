# ===== CLASS =====
# работи с класа, а не с инстанциите
# може да прави инстанции от същият клас
# вграден декоратор


class Laptop:
    made_in = "Germany"

    def __init__(self, memory:int, model:str):
        self.memory = memory
        self.model = model

    @classmethod    # създава точно определена инстанция на класа
    def low_ram_laptop(cls):
        return cls(256, "Asus")

    @classmethod
    def made_in_other(cls):
        cls.made_in = "China"
        return f"{cls.made_in}"


small_laptop_1 = Laptop.low_ram_laptop()
print(small_laptop_1)

laptop_1 = Laptop(512, "Model 3")
print(laptop_1)

laptop_2 = Laptop.made_in_other
print(laptop_2)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod    # работи с статик метода
    def from_birth_year(cls, name, birth_year):
        age = cls.calculate_age(birth_year)
        return cls(name, age)

    @staticmethod
    def calculate_age(birth_year):
        current_year = 2023  # Текущата година (може да бъде заменена със функция за взимане на текущата година)
        return current_year - birth_year




person_1 = Person("Ivan", 28)
# print(person_1.age)

person_2 = Person.from_birth_year("Alice", 1990)
# print(f"{person_2.name} is {person_2.age} years old.")






# ===== STATIC =====
# независима от класа функция, може да си същ. извън класа,
# не ползва класа или инстанцийте, може да живее сама
# слага се в класа само защото е близък по логика с класа

from functools import reduce
class Calculator:

    @staticmethod
    def add_nums(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply_nums(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide_nums(*args):
        return reduce(lambda x, y: x / y, args)

# print(Calculator.add_nums(1, 2, 3, 4, 5))
# print(Calculator.multiply_nums(1, 2, 3, 4, 5))
# print(Calculator.divide_nums(1, 2, 3, 4, 5))




class Person:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age

    @staticmethod  # име на декоратора
    def is_adult(age):
        return age >= 18

persona_1 = Person("Ivan", 20)
# задавам стойността 5, викам през класа не през инстанцията
# print(Person.is_adult(5))


