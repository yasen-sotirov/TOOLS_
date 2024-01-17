

class Employee:
    company = "DSK"
    def __init__(self, name: str, family: str, password, salary: int):
        if len(name) > 3:
            self._name = name       # instance attribute
        self.family = family        # public instance attribute
        self._password = password   # protected instance attribute
        self.salary = salary        # property, защото има setter и няма подчертавка
                                    # при инициализиране подава на setter-a, който валидира

    @property                   # първо getter, после setter
    def salary(self):
        return self._salary     # instance attribute

    @salary.setter              # задължително е прикачен към getter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Без пари не става!")
        self._salary = value    # instance attribute

    @property                   # декоратор
    def name(self):
        return self._name       # instance attribute

    @property                   # read-only, няма си setter
    def full_name(self):        # зад property не е задължително за има атрибут
        return f'{self.name} {self.family}'

    def __password_is_correct(self, old_password):      # private метод видим само в класа
        return self._password == old_password           # същото: като if self._password == old_password:



employee_1 = Employee("Ivan", "Petrov", "pass123", 1_500)


"ПРОМЯНА НА АТРИБУТИ SETTER"
# employee_1.salary = employee_1.salary + 300
# employee_1.salary = 0         # промяната не минава заради валидациите ни
# print(employee_1.salary)


"ПРЕСКАЧАНЕ НА SETTER"          # директно достъпване до вътрешния атрибут
# employee_1._salary = 0
# print(employee_1.salary)


"READ-ONLY АТРИБУТИ"            # само през getter и не може да се променя след инициализация
# print("employee_1 name", employee_1.name)
# employee_1.name = 'Todor'     # AttributeError: property 'name' of 'Employee' object has no setter


"NAME MANGLING - ПОГРОЗНЯВАНЕ"          # дава достъп до __private атрибутите
# print(employee_1.password)              # AttributeError: 'Employee' object has no attribute 'password'
# print(employee_1._Employee__password)   # прави възможно достъпването на protected attribute


"ИЗКЛЮЧЕНИЕ"        # това записване всъщност създава нов атрибут (чужд на класа)
                    # който не е равен на атрибута _password
# employee_1.password = "123pass"
# print(employee_1.password)