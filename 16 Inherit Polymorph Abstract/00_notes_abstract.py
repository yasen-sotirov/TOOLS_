"""


ЕНКАПСУЛАЦИЯ
    групиране на състояние и поведение в рамките на класове
    скриване и защита от външния свят (света извън класа)
    Енкапсулацията е подхода който помага да групираме състоянието
    и поведението на обектите в един клас


АБСТРАКЦИЯ
    Логиката на програмата
    къде какво се случва
    технически как се случват нещата не ни интересуват на това ниво

"""


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


