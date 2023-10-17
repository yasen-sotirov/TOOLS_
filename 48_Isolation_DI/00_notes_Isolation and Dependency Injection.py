"Isolation and Dependency Injection"    # записки с Едо

"""
втората функция работи в зависимост от първата функция

3 вида Dependency Injection (зависимост) :
- в конструктура на класа - най-често се ползва
- в сетъра на класа
- в метод на класа

business logic == работна логика
"""


class Truck:
    def __init__(self, id, name):
        self.id = id
        self.name = name

trucks = [Truck(1, 'A'), Truck(2, 'B')]
# dependat


# dependency
class FileWrite:
    def write(self, trucks: list[Truck]):
        with open('data.csv', 'w+') as f:
            pass









































