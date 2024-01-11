"Isolation and Dependency Injection"    # записки с Едо

"""
DEPENDENCY INJECTION
Един класове или функции използва като параметър други клас/функция.
Втората функция работи в зависимост от първата функция.

- дава възможност докато работи кода да ползва един или друг клас
- Ползва се и когато се налага зависимите класове да се подменят, 
  без да се влиза в основния код


DEPENDENCY - За да работи един клас има нужда от друг клас
    три вида Dependency Injection (зависимост) :
    - в конструктура на класа - най-често се ползва
    - в сетъра на класа
    - в метод на класа
    
    business logic == работна логика



ВИДОВЕ DEPENDENCY
    STABLE - може да предвидим крайния резултат
    
    VOLATILE - не можем да контролираме какъв ще е крайния резултат
        date time
        user imput
        http заявки



ИЗОЛАЦИЯ - когато искаме да изолираме клас от неговите dependency
    в unit test-а изолираме (подменяме) volatile с фалшиви stable dependency-та 
    за да не ги развалим по време на тестването. 
    За нуждите на теста ползваме фалшиви dependency-та: mock







"""


class Truck:
    def __init__(self, id, name):
        self.id = id
        self.name = name

trucks = [Truck(1, 'A'), Truck(2, 'B')]


"DEPENDANT" # зависимият клас





"DEPENDENCY"

# писане във файл
class FileWrite:
    def write(self, trucks: list[Truck]):
        lines = ['id, name'] + [f'{truck.id}, { truck.name}' for truck in trucks]
        with open('data.csv', 'w+') as f:
            f.write('\n'.join(lines))

# писане в конзола
class ConsoleWrite:
    def write(self, trucks: list[Truck]):
        for truck in trucks:
            print(truck.id, truck.name)


write = ConsoleWrite()
write.write(trucks)






"MOCKING"
'''
създаване на фалшив обект имитиращ истински 
'''






































