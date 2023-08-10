"FILTER"

line = [1, 15, 2, 8, 31, 5, 9]
# 1. Filter all the numbers which are less than 5 or larger than 15
print(list(filter(lambda num: num < 5 or num > 15, line)))


# 2. Filter all the numbers which are larger than 5 and less than 15.
print(list(filter(lambda num: 5 < num < 15, line)))


# 3. Filter all the numbers which are prime.
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
print(list(filter(lambda num: is_prime(num), line)))


# 4. Filter all the strings which longer than 5 symbols.
str_line = ['cat', 'dog', 'elephant', 'cucumber']
print(list(filter(lambda el: len(el) > 5, str_line)))

# 5. Filter all the strings that include a certain substring.
word_line = ['cat', 'dog', 'duck', 'cucumber']
def find_sub_str(el):
    sub_str = "uc"
    if sub_str in el:
        return el
    return False
print(list(filter(lambda el: find_sub_str(el), word_line)))


"MAP"
# 1. Double each number in an list of numbers.
line = [1, 2, 3, 4]
print(list(map(lambda num: num * 2, line)))


# 2. Uppercase each string in a list of strings.
word_line = ['cat', 'dog']
print(list(map(lambda el: el.upper(), word_line)))


# 3. Transform each string to the opposite case.
opposite_list = ['cat', 'DOG']
def convert(el):
    if el.islower():
        return el.upper()
    return el.lower()
print(list(map(lambda el: convert(el), opposite_list)))


# Normalize each string. Normalization means taking a string containing
# any case letters and making it capitalized.
normal_line = ['eLepHANT', 'CucuMbeR']
print(list(map(lambda word: word.capitalize(), normal_line)))




"REDUCE"
from functools import reduce

# 1. Return the product of an list of numbers.
multiply_num = [1, 2, 3, 4, 5]
print(reduce(lambda num_1, num_2: num_1 * num_2, multiply_num))

# 2. Return the maximum number in a list of numbers.
# Hint: with reduce you can also replace the result of the previous iteration.
max_list = [7, 13, 72, 14]
print(reduce(lambda x, y: x if x > y else y, max_list))


# 3. Return the longest string in a list of strings.
long_list = ['cat', 'dog', 'elephant', 'cucumber']
print(reduce(lambda w1, w2: w2 if len(w1) > len(w2) else w2, long_list))


# 4. Reverse a string. Hint: A string is just a list of characters.
# To use reduce on a string, you can spread it a list like this: [...'apple'].reduce(...

