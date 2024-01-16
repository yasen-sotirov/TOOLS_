

class Employee:
    def __init__(self, name: str, family: str, salary: int):
        self.name = name
        self.family = family
        self._salary = salary


    @property               # read-only, няма си setter
    def full_name(self):    # зад property не е задължително за има атрибут
        return f'{self.name} {self.family}'


    @property
    def salary(self):
        return self._salary

    @salary.setter          # задължително е прикачен към getter
    def salary(self, value):
        min_salary = 1000
        max_salary = 3000
        if min_salary < value < max_salary:
            self._salary = value


employee_1 = Employee("Ivan", "Petrov", 1_500)
employee_2 = Employee("Petar", "Georgiev", 2_000)


"ИЗВИКВАНЕ НА GETTER"
print(employee_1.salary)

"ИЗВИКВАНЕ НА SETTER"
