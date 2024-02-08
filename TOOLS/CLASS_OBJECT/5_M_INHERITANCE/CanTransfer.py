from Account import Account
class CanTransfer:
    def transfer(self, transfer: int, other_account: Account):
        if transfer < 0:
            raise ValueError('Invalid value')
        if self.balance < transfer:
            raise ValueError('Invalid value')

        self.balance -= transfer
        other_account.deposit(transfer)
