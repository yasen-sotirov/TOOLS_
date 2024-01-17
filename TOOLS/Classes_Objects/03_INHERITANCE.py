"INHERITANCE"   # наследяване
                # наследява атрибути и методи
                # може да дефинира нови атрибути и методи а съществуващите да бъдат променени
                # полза: преизползване на код
                # super - извиква атрибутите на базовия клас
                # IS-A връзка: Мениджърът Е Служител
                # Може да имаме Полиморфизъм в два класа, който нямат общ родител.


class Employee:         # базов клас
    COMPANY = "DSK"
    def __init__(self, name: str, salary: int, department: str):
        self.name = name
        self.salary = salary
        self.department = department

    def public_info(self):
        return f'{self.name} {self.department}'

    def private_info(self):
        return f'{self.name} {self.department} {self.salary}'



class CustomerSupport(Employee):
    def __init__(self, name, salary, department, email: str, phone_number: int):
        super().__init__(name, salary, department)      # извиква атрибутите на базовия клас
        self.email = email
        self.phone_number = phone_number

    def contacts(self):
        return f'{self.name}, {self.email}, {self.phone_number}'



class Manger(Employee):
    def __init__(self, name, salary, department):       # не подавам нови атрибути
        super().__init__(name, salary, department)
        self.employees_list = []

    def add_employee(self, new_employee):
        self.employees_list.append(new_employee)



support = CustomerSupport("Jordan", 3000, "sales", "example@mail.com", 359888123456)

# print(support.contacts())



