from Account import Account
from CanTransfer import CanTransfer

class PremiumAccount(Account, CanTransfer):
    # наследил е всичко което му трябва
    # комбинираме нужните ни методи за да създадем специален клас
    pass


account_1 = Account()
account_1.deposit(20)
account_1.withdraw(5)
print(account_1)
