class EmployeeWithProperties:
    def __init__(self, full_name, salary, department):
        self._full_name = full_name
        self._department = department
        self.salary = salary

    # readonly property
    @property
    def full_name(self):
        return self._full_name

    # readonly property
    @property
    def department(self):
        return self._department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 500:
            self._salary = value

    def public_info(self):
        # името и департамента вече реферират към property метода, ане към self. метода
        return f'{self.full_name}, Department: {self.department}'

    def internal_info(self):
        return f'{self.public_info()}, Salary: {self.salary}'
