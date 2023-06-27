""" 1. Write a function that sums only the digits in a string

x = sum_digits('abc123a4') # x = 10
x = sum_digits('abc') # x = 0"""


def is_digit(data):
    counter = 0
    for el in data:
        if el.isdigit():
            el = int(el)
            counter += el
    return counter


input_data = input()
print(is_digit(input_data))
