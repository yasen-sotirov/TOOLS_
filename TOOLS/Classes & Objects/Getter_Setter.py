class Employee:

    def __init__(self, name, salary):
        if name == "":
            raise ValueError("need real name")
        self._name = name
        self.salary = salary    # стойността вече се взема от setter -a


    @property       # READ-ONLY с проверка
    def name(self):
        return self._name


    @property           # стойността вече се взема от setter -a
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("salary cant be negative")
        self._salary = value


a = 5
employee_1 = Employee("Tosho", 500)
print(employee_1.salary)
print(employee_1.name)


