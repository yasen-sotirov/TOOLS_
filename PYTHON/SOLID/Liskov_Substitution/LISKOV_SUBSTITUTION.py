"LISKOV SUBSTITUTION"   # LSP
# всички елементи на базовия клас трябва да бъдат валидни за наследниците
# наследяващите класове само разширяват функционалността на базовия клас


from abc import ABC, abstractmethod

class Animal(ABC):          # Абстрактен клас - абстракция
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def fly(self):
        pass


class Dog(Animal):              # няма нужда от проверка на вида животно: без if-ве
    def make_sound(self):       # полиморфизъм - пренаписваме функционалността на метода
        return "wof wof"
    def fly(self):              # нарушава LSP: базовият метод не е приложим за наследника
        return "I can't fly"


class Cat(Animal):
    def make_sound(self):       # полиморфизъм
        return "meow"
    def fly(self):
        return "I can't fly"    # нарушава LSP: базовият метод не е приложим за наследника


class Lamia(Animal):
    def make_sound(self):       # полиморфизъм
        return 'Ssssssss'
    def fly(self):
        return "Flying!"



def flying(animals_list: list):
    for animal in animals_list:
        print(animal.fly())


animals = [Dog(), Cat(), Lamia()]
flying(animals)








