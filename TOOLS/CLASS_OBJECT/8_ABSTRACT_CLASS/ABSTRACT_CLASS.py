"АБСТРАКТНИ КЛАСОВЕ"    #

'''
Клас, който се използва само за дефиниране на интерфейс, 
като не се разписва конкретна имплементация на неговите методи. 
Използва се като шаблон, от който други класове могат да наследяват 
и да реализират методите според своите специфични изисквания.

Всички методи задължително трябва ад бъдат наследени

Създава се чрез модула abc (Abstract Base Classes)

Насърчава Полиморфизъм  
  '''

from abc import ABC, abstractmethod


class Shape(ABC):           # клас шаблон
    @abstractmethod
    def area(self):         # не се разписва конкретна имплементация
        pass

    @abstractmethod
    def perimeter(self):    # не се разписва конкретна имплементация
        pass


'''super() ни позволява да извикваме методите от родителския клас, 
преди да извикаме собствените методи на детския клас.'''


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):         # реализира методa според своите спец. изисквания
        return self.width * self.height

    def perimeter(self):    # реализира методa според своите спец. изисквания
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):         # реализира методa според своите спец. изисквания
        return 3.14 * self.radius * self.radius

    def perimeter(self):    # реализира методa според своите спец. изисквания
        return 2 * 3.14 * self.radius


# Пример за използване на абстрактен клас
# shape = Shape()  # Това ще генерира грешка, защото не можем да създадем инстанция на абстрактен клас

rectangle = Rectangle(5, 4)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

circle = Circle(3)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.perimeter())
