"COMPOSITION"   # техника за преизползване на код
# един клас използва обекти на други класове,
# като стойности на атрибути
# т.е. един комплексен обект е изграден от няколко прости обекти
# релация HAS-A
# няма специален синтаксис
# при промяна на метод
# Композицията позволява по-голяма гъвкавост и отделение на отговорностите в
# сравнение с наследяването, тъй като не създава тясна връзка между класовете.
# защото промените в класа на компонента рядко засягат съставния клас,
# а промените в съставния клас никога не засягат класа на компонента.



class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")



class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car is starting")
        self.engine.start()

    def stop(self):
        print("Car is stopping")
        self.engine.stop()




# Използване на композиция
my_car = Car()
my_car.start()
my_car.stop()



class Address:
    def __init__(self, street, number,city):
        self.street = street
        self.number = number
        self.city = city

    def __str__(self):
        return (f'# {self.number} {self.street}, \n'
                f'{self.city} city.')


class Position:
    def __init__(self, p_name, salary):
        self.p_name = p_name
        self.salary = salary

    def __str__(self):
        return (f'position: {self.p_name} \n'
                f'salary: {self.salary}')


class Employee:
    def __init__(self, name, position: Position, address: Address):
        self.name = name
        self.position = position
        self.address = address


address = Address('Baker street', 8, 'London')
position = Position('Manager', 2_000)
employee = Employee('Ivanov', position, address)

print(employee.address)
print(employee.position)





