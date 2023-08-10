from functools import reduce

number_list = [1, 2, 4, 5, 6, 11, 9, 8]

def get_even(num):
    return num % 2 == 0

result = list(filter(get_even, number_list))
print(result)


result_lambda = list(filter(lambda num: num % 2 == 0, number_list))
print(result_lambda)


line = ["abc", "1", "2.5", "5"]
numbers = list(filter(lambda num: num.isnumeric(), line))

# само int   num.isdgit()
# numbers.isallnum()
# number.isdecimal()
# numbers.is digit
# number.


print(reduce(lambda x, y: x + y, number_list))
