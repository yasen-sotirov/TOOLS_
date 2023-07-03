"""
Write a list comprehension that filters all the numbers which are prime.
You will need an is_prime function to use in the conditional part

[1,15,2,8,31,5,9] -> [2,31,5]
"""


def is_prime_num(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for idx in range(2, number):
        if number % idx == 0:
            is_prime = False
    if is_prime:
        return True
    else:
        return False


lst = [1, 15, 2, 8, 31, 5, 9]
print([x for x in lst if is_prime_num(x)])

