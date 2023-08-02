
class Employee:         # дефиницията от класа я пишем в отделен файл
    """ ДОКУМЕНТАЦИЯ НА КЛАСА: ала - бала, дрън - дрън ..."""
    # КОНСТАНТИТЕ СЕ ПИШАТ С ГЛАВНИ БУКВИ
    num_of_employee = 0     # клас атрибут/променлива, която се дефинира в тялото на класа
    company_name = "OMV"    # важно е да се достъпват и променят през името на класа, а не през името на инстанцията

    # за прегледност се пише преди инита
    @classmethod        # метода принадлежи на класа и е валиден за всички инстанции
    def create_id(cls):
        cls.num_of_employee += 1
        employee_id = cls.num_of_employee
        return employee_id

    # init метода се извиква веднъж при създаването на обекта - конструктор
    # self. реферира към текущата инстанция. към self закачаме името на променливата "employee_1"
    def __init__(self, first_name, second_name, position, salary):     # конструктор, инициализатор
        self.first_name: str = first_name    # employee_1.first_name = first_name
        self.second_name: str = second_name  # employee_1.second_name = second_name
        self.position: str = position        # employee_1.position = position
        if salary < 0:
            raise ValueError("The salary must be positive number")
        self.salary: int = salary            # employee_1.salary = salary
        self.traker = []                     # employee_1.traker = []
        # Employee.num_of_employee += 1         # може и така да се напише, но е по-добре с клас метод
        # self.id = Employee.num_of_employee
        self.id = Employee.create_id()
        self.number = Employee.num_of_employee    # клас атрибута(променливата) я достъпваме през името на класа

    def work(self, hrs: int):    # метод - определя поведението (behavior)на обекта
        self.traker.append(hrs)

    def __str__(self):      # трябва да се пренапише иначе връща мястото на обекта
        return f"Employee name: {self.first_name} " \
               f"on position {self.position} has worked {self.traker} at company {Employee.company_name}"

    def __eq__(self, other_employee):
        return self.__str__() == other_employee.__str__()

    def __le__(self, other):
        return self.salary, other.salary

    def __ge__(self, other):
        return self.salary, other.salary

    def __gt__(self, other):
        return self.salary, other.salary

    @property       # read-only property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    @property       # getter - подава параметър
    def change_name(self):
        return f"Second name {self.second_name}"

    @change_name.setter     # setter - задава параметър
    def change_name(self, new_name):
        self.second_name = new_name


employee_1 = Employee("Gosho", "Petrov", "dev", 1000)
employee_2 = Employee("Pesho", "Ivanov", "manager", 1500)
employee_3 = Employee("Tosho", "Todorov", "seo", 2000)     # има обекта, но е недостъпен, защото не е рефериран
employee_4 = Employee("Ivanka", "Petrova", "dev", 2500)
employee_4_1 = Employee("Ivanka", "Petrova", "dev", 2500)
# print(employee_1.company_name)


"MAGIC МЕТОД __str__"       # трябва да се пренапише иначе връща мястото на обекта
# print(employee_1)
# print(employee_2)
# print(employee_3.__str__())     # малко по-дълго изписване


"__dict__ ВРЪЩА ОБЕКТА КАТО РЕЧНИК"
# print(employee_1.__dict__)

"__doc__ ВРЪЩА ДОКУМЕНТАЦИЯТА НА КЛАСА"
# print(Employee.__doc__)

"__eq__ == "
print(employee_4 == employee_4_1)

"__le__ <= "
print(employee_1 <= employee_2)

"__ge__ >= "
print(employee_4 >= employee_4_1)

"__gt__ > "
print(employee_1 > employee_2)



"ПРОМЯНА ЧРЕЗ SETTER и GETTER"
# print(employee_4.full_name)
# employee_4.change_name = "Petrova - Ivanova"
# print(employee_4.full_name)


# Клас методите и клас атрибутите действат на целия клас и са валидни за всички инстанции на класа
# клас метода НЕ се влияе от инстанциите на класа

# в Питон може през обектите да извикаме клас атрибути
# print(gosho.num_of_employee)
#
# print(employee_1.id)


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







