""" 1. Write a function that sums only the digits in a string

x = sum_digits('abc123a4') # x = 10
x = sum_digits('abc') # x = 0"""


def is_digit(data):
    sum_nums = 0
    for el in data:
        if el.isdigit():
            el = int(el)
            sum_nums += el
    return sum_nums


input_data = input('tape nums: ')
print(is_digit(input_data))
