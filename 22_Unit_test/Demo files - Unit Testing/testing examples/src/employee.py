class Employee:
    def __init__(self, full_name, salary, department):
        self.full_name = full_name
        self.department = department
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 500:
            raise ValueError('Salary must be greater than 500')

        self._salary = value

    def info(self):
        return f'{self.full_name}, Department: {self.department}'

