from account import Account
from premium_account import PremiumAccount


account = Account() # (CanDeposit, CanWithdraw)
account.deposit(20)
account.withdraw(5)
# account.print_me()
print(account)

premium_account = PremiumAccount() #(Account, CanTransfer)
premium_account.deposit(15)
premium_account.transfer(10, account)
print(premium_account)
print(account)
