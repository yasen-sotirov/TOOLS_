class CanDeposit:
    def deposit(self, deposit: int):
        if deposit < 0:
            raise ValueError("Invalid value")
        self.balance += deposit


