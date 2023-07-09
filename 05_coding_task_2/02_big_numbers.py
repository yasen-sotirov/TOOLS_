"""
Big Numbers
Write a method that adds two positive integer numbers represented as arrays of
digits (each array element arr[i] contains a digit; the last digit is kept
in arr[0]). Write a program that reads two arrays representing positive integers
and outputs their sum.
Input
    On the first line you will receive two numbers separated by spaces -
    the size of each array
    On the second line you will receive the first array
    On the third line you will receive the second array

Output
    Print the sum as an array of digits (as described)
        Digits should be separated by spaces

Constraints
    Each of the numbers that will be added could have up to 10 000 digits.

Sample tests
Input
3 4
8 3 3
6 2 4 2

Output
4 6 7 2

Input
5 5
0 3 9 3 2
5 9 5 1 7

Output
5 2 5 5 9


Input
5 3
6 2 4 2 2
8 3 3

Output
4 6 7 2 2

Input
3 5
8 3 3
6 2 4 2 2

Output
4 6 7 2 2
"""


num_1_length, num_2_length = [int(x) for x in input().split()]
first_num = [int(x) for x in input().split()]
second_num = [int(x) for x in input().split()]

# проверка за разлика в дължината на листовете, за да не гръмне по индекс
difference = num_1_length - num_2_length

# добавям необходимите нули, за да изравни
if difference < 0:
    add = [0] * abs(difference)
    first_num += add

elif difference > 0:
    add = [0] * difference
    second_num += add


in_mind = 0

# няма значение кой списък, защото те са изравнени като дължина
for index in range(len(first_num)):
    result = first_num[index] + second_num[index] + in_mind
    # редуцира до единици
    print(result % 10, end=' ')

    in_mind = 1 if result > 9 else 0
