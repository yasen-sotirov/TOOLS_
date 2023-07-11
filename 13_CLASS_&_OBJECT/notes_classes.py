# В Питон всичко е обект

class Employee:         # дефиницията от класа я пишем в отделен файл
    # КОНСТАНТИТЕ СЕ ПИШАТ С ГЛАВНИ БУКВИ
    num_of_employee = 0     # клас атрибут, променлива, която се дефинира в тялото на класа

    # за прегледност се пише преди инита
    @classmethod        # метода принадлежи на класа и е валиден за всички инстанции
    def create_id(cls):
        cls.num_of_employee += 1
        employee_id = cls.num_of_employee
        return employee_id

    # init метода се извиква веднъж при създаването на обекта
    def __init__(self, first_name, second_name, position, salary):     # конструктор, инициализатор
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.position: str = position
        if salary < 0:
            raise ValueError("The salary must be positive number")
        self.salary: int = salary
        self.traker = []
        # Employee.num_of_employee += 1         # може и така да се напише, но е по-добре с клас метод
        # self.id = Employee.num_of_employee
        self.id = Employee.create_id()

    def work(self, hrs: int):        # метод - определя поведението (behavior)на обекта
        self.traker.append(hrs)

    def __str__(self):
        return f"Employee name: {self.first_name} " \
               f"on position {self.position} has worked {self.traker}"

    def view(self):
        return f"Employee name: {self.first_name} " \
               f"on position {self.position} has worked {self.traker}"

    def __eq__(self, other_employee):
        if not isinstance(other_employee, Employee):
            return False
        return other_employee.first_name == self.first_name and other_employee.id == self.id

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    @property
    def change_name(self):
        return f"Second name {self.second_name}"

    @change_name.setter
    def change_name(self, new_name):
        self.second_name = new_name


gosho = Employee("Gosho", "Petrov", "dev", 1000)
pesho = Employee("Pesho", "Ivanov", "manager", 1000)
tosho = Employee("Tosho", "Todorov", "seo", 1000)     # има обекта, но е недостъпен, защото не е рефериран
ivanka = Employee("Ivanka", "Petrova", "dev", 1000)


"MAGIC МЕТОД __str__"
# print(gosho.view())     # така е пренаписано, малко по-дълго е
# gosho.work(2)
# print(gosho)            # защото има разписан __str__ метод


"ПРОМЯНА ЧРЕЗ SETTER и GETTER"
# print(ivanka.full_name)
# ivanka.change_name = "Petrova - Ivanova"
# print(ivanka.full_name)


# Клас методите и клас атрибутите действат на целия клас и са валидни за всички инстанции на класа
# клас метода НЕ се влияе от инстанциите на класа

# в Питон може през обектите да извикаме клас атрибути
# print(gosho.num_of_employee)
#
# print(gosho.id)


"РЕФЕРЕНЦИИ НА IMMUTABLE ОБЕКТИ"
# не променяме обектите, а референциите, които сочат към тях
# x = 5   # х реферира към 5
# y = x   # y реферира към 5 също
# x = 6   # х вече реферира към 6, а y продължава да реферира към 5


"РЕФЕРЕНЦИИ НА MUTABLE ОБЕКТИ"
# # не променяме обектите, а референциите,
# # които сочат към тях
# x1 = [1, 2, 3]
# y1 = x1          # y1 реферира към х1 също
# # или x1 = y1 = [1, 2, 3]
#
# x1.append(4)
# print(y1)        # [1, 2, 3, 4]
#
# y1.append(5)
# print(x1)       # [1, 2, 3, 4, 5]

# прави копие на листа, слайсва открай докрай
# my_list = [5, 6, 7]
# list_copy = my_list[:]
# list2_copy = my_list.copy()


# def change():
#     # излиза от локалния scope на функцията и търси в глобалния
#     lst1.append(3)
#
# lst1 = [1, 2]
# change()
# print(lst1)     # [1, 2, 3]


"ПРОВЕРЯВА ДАЛИ ОБЕКТ Е ИНСТАНЦИЯ НА КЛАСА __eq__"
