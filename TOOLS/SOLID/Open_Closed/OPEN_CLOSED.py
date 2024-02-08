"OPEN CLOSED"   # Open for extension, but closed for modification
# При нужда от нова логика допълваме,
# но не променяме старата, защото не знаем какво ще счупим

'''
ПОСТИГА СЕ ЧРЕЗ:
Abstraction
Mix-ins
Monkey-Patching
Generic functions (using overloading)
'''

class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4



"РАЗШИРЯВАНЕ НА СЪЩ. ФУНКЦИОНАЛНОСТ" # без да пипаме старата
class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        super().get_discount()          # наследяване на метод
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


discount = AdditionalDiscount('Test', 1000, 4.68)
print(discount.get_discount())




'''=== ПРИМЕР 2 ===
При така подреден кода може да добавяме колкото искаме
нови животни: Open for Extension

Няма нужда да променяме съществуващи класове и методи
спазваме Closed for Modification

'''
from abc import ABC, abstractmethod

class Animal(ABC):          # Абстрактен клас - абстракция
    @abstractmethod
    def make_sound(self): pass

class Dog(Animal):              # няма нужда от проверка на вида животно: без if-ве
    def make_sound(self):       # полиморфизъм - пренаписваме функционалността на метода
        return "wof wof"

class Cat(Animal):
    def make_sound(self):       # полиморфизъм
        return "meow"

class Lamia(Animal):
    def make_sound(self):       # полиморфизъм
        return 'Ssssssss'


def animal_sounds(animals: list):   # затворен за модификация - няма какво да му пипаме за да работи с което и да е ново допълнение
    for animal in animals:
        print(animal.make_sound())


animal_list = [Dog(), Cat(), Lamia()]
animal_sounds(animal_list)

