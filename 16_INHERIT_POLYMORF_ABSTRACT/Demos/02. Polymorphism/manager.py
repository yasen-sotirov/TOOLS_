from employee import Employee


class Manager(Employee):
    def __init__(self, full_name, salary, department):
        super().__init__(full_name, salary, department)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    # overridden
    def public_info(self):
        dep_text = f'{self.department} ({len(self.employees)} employees)'

        return f'{self.full_name}, Manager of {dep_text}'
