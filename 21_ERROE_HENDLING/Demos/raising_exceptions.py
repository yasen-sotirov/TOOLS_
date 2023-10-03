def deposit_money(amount):
    if amount < 0:
        raise ValueError('Must deposit positive amount')
    
    # deposit somewhere ....
    print(f'Deposited {amount}')


# handle
amounts = [300, -200, 400]
try:
    for amount in amounts:
        deposit_money(amount)
except ValueError as e:
    print(e)
print() # just a blank line




# or validate before causing exceptions
for amount in amounts:
    if amount > 0:
        deposit_money(amount)