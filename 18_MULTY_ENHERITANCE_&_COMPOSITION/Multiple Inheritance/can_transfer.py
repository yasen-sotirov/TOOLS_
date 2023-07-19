from account import Account


class CanTransfer:
    def transfer(self, money: int, other_account: Account):
        if money < 0:
            raise ValueError('Invalid value')
        if self.balance < money:
            raise ValueError('Balance too low')

        self.balance -= money
        other_account.deposit(money)
