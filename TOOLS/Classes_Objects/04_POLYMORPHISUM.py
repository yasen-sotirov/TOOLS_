"ПОЛИМОРФИЗЪМ"      # наследникът override-ва базовите методи
                    # override метод трябва да връща същия тип данни
                    # съкращава писането на код

class CreditCard:
    BANK = "UCB"
    def __init__(self, name: str, number: int, pin):
        self.name = name
        self.number = number
        self.pin = pin

    def public_info(self):
        return f"{self.name}, {self.number}"


class ChildCreditCard(CreditCard):
    def __init__(self, name, number, pin, child_name: str):
        super().__init__(name, number, pin)
        self.child_name = child_name

    def public_info(self):
        return f'{super().public_info()}, {self.child_name}'    # съкратено включва наследения метод


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []

    def public_info(self):      # полиморфизъм между несвързани класове
        return f'{self.name}, {self.address}'


child_card = ChildCreditCard("Ivan", 1234_1234_1234_1234, 4321, "Ivancho J")
print('кредитна карта', child_card.public_info())

library = Library('P. Slaveikov', "Sofia")
print('библиотека', library.public_info())
