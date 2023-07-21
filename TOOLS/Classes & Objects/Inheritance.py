"""
НАСЛЕДЯВАНЕ
    може да наследим един клас когато отговаря на въпроса IS - A
    мениджъра служител ли е?
    чистача служител ли е?
"""


class Employee:
    def __init__(self, full_name, salary, department):
        self.full_name = full_name
        self.department = department
        self.salary = salary

    def public_info(self):
        return f'{self.full_name}, Department: {self.department}'

    def internal_info(self):
        return f'{self.public_info()}, Salary: {self.salary}'



class Manager(Employee):
    def __init__(self, full_name, salary, department):
        super().__init__(full_name, salary, department)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)



class CustomerSupport(Employee):
    def __init__(self, full_name, salary, department, email, phone_number):
        super().__init__(full_name, salary, department)
        self.email = email
        self.phone_number = phone_number

    def contacts(self):
        return f'{self.full_name}, Email: {self.email}, Phone: {self.phone_number}'




employee = Employee('Peter Griffin', 2000, 'Quality Control')
manager = Manager('John Smith', 2000, 'Quality Control')
customer_support = CustomerSupport('Gregory House', 2000, 'Quality Control', 'gregory@qc.company', '071238123')

# inherited attributes and methods
print(manager.public_info())
print(manager.internal_info())
print(manager.salary)
print(customer_support.public_info())
print(customer_support.internal_info())
print(customer_support.salary)

# Manager-only attributes and methods
manager.add_employee(employee)
manager.add_employee(customer_support)
print(len(manager.employees))

# CustomerSupport-only attributes and methods
print(customer_support.phone_number)
print(customer_support.contacts())
