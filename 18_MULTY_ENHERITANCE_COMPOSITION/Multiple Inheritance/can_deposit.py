class CanDeposit:
    def deposit(self, money):
        if money <= 0:
            raise ValueError('Invalid value')

        # duck typing in action - you have 'balance', then you are account
        self.balance += money
