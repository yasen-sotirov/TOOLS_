class CanWithdraw:
    def withdraw(self, money):
        if money <= 0:
            raise ValueError('Invalid value')
        if self.balance < money:
            raise ValueError('Balance too low')

        # duck typing in action - you have 'balance', then you are account
        self.balance -= money

