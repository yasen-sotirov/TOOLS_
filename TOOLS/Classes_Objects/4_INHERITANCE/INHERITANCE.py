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
    def __init__(self, name, salary, department, bonus: int):       # не подавам нови атрибути
        super().__init__(name, salary, department)
        self.bonus = bonus
        self.employees_list = []

    def add_employee(self, new_employee):
        self.employees_list.append(new_employee)



support_1 = CustomerSupport("Jordan", 3000, "sales", "example@mail.com", 359888123456)
# print(support_1.contacts())

# manager_1 = Manger("Todor", 4000, "managers", 300)
# manager_1.add_employee(support_1.name)
# print(manager_1.employees_list)


"MIXIN"
class CEO:
    def fire_employee(self, employee):
        return f"{employee.name} was fired."
        del employee


class TopManager(Manger, CEO):
    def __init__(self, name, salary, department, bonus):
        super().__init__(name, salary, department, bonus)

ceo_1 = TopManager('Georgiev', 5000, 'managers', 500)
ceo_1.fire_employee(support_1)
print(support_1)


