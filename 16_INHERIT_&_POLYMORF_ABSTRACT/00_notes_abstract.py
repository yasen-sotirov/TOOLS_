from abc import ABC, abstractmethod
# задължава всеки от наследниците класове да има този метод


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return "area"


class Circle(Shape, ABC):
    def __init__(self, radius):
        self.radius = radius

    def calculate(self):
        return f"{self.radius} + {Shape.calculate_area()}"


