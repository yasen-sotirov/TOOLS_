"MULTIPLE INHERITANCE"   # множествено наследяване
# разпределянето на методите в различни класове дава възможност
# да създадем къстъм класове от тези градивни елементи


from CanDeposit import CanDeposit
from CanWithdraw import CanWithdraw


class Account(CanDeposit, CanWithdraw):
    def __init__(self):
        self.balance = 0

    def __str__(self):
        return f'Current {type(self).__name__} balance: {self.balance}'


