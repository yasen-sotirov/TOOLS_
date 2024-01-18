class CanWithdraw:
    def withdraw(self, withdraw: int):
        if withdraw < 0:
            raise ValueError('Invalid value')
        if self.balance < withdraw:
            raise ValueError('Balance too low.')
        self.balance -= withdraw


