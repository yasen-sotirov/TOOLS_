# обектите имат състояние и поцедение
#

class Employee:

    def __init__(self, full_name: str, salary: int, department: str):
        self.full_name = full_name
        self.salary = salary
        self.department = department

    def public_info(self):
        pass


class Manger(Employee):
    def __init__(self, full_name: str, salary: int, phone, num, department=None):
        super().__init__(full_name, salary, department)
        self.employee = []
        self.phone = phone
        self.num = num

    def add_employee(self, employee):
        self.employee = employee


object_employee_1 = Employee("Todor Todorov", 1500, "QA")
object_manager_1 = Manger("Ivan Ivanov", 1500)
