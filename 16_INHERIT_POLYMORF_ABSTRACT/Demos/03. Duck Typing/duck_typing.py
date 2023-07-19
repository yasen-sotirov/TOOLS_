from math import pi as PI


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return (self.base * self.height) / 2


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * PI


for shape in Circle(5), Rectangle(3, 8), Triangle(2, 4):

    # all objects define the area property
    # it would work for methods and/or attributes also
    print(f'{shape.area:.4f}')
