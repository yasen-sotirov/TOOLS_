from can_deposit import CanDeposit
from can_withdraw import CanWithdraw


class Account(CanDeposit, CanWithdraw):
    def __init__(self):
        self.balance = 0

    def __str__(self):
        return f'Current {type(self).__name__} balance: {self.balance}'
