"""
Write a list comprehension that filters all the users that have strong passwords.
A 'strong' password means one lowercase, one uppercase, one digit and at least
8 symbols long.

[('pesho', 'qwe345!'), ('gosho', 'passwOrd1'), ('penka', '1a2b3c4d')]

[('gosho', 'passwOrd1')]
"""

all_users = [('pesho', 'qwe345!'), ('gosho', 'passwOrd1'), ('penka', '1a2b3c4d')]

print([(user, password) for (user, password) in all_users if len(password) >= 8 and any(digit.islower() for digit in password) and any(digit.isupper() for digit in password) and any(digit.isnumeric() for digit in password)])
