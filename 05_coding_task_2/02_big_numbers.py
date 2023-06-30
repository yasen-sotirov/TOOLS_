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
"""

num_1, num_2 = [int(x) for x in input().split()]
result_num = []
in_mind = 0

first_num = [int(x) for x in input().split()]
second_num = [int(x) for x in input().split()]

if num_1 == num_2:
    index = 0
    for el in range(num_1):
        sum_num = first_num[index] + second_num[index]
        digit_1 = sum_num // 10
        digit_2 = sum_num % 10

        result_num.append(digit_2 + in_mind)
        index += 1
        in_mind = digit_1

else:
    for el in range(min(num_1, num_2)):
        sum_num = first_num[0] + second_num[0]
        digit_1 = sum_num // 10
        digit_2 = sum_num % 10

        result_num.append(digit_2 + in_mind)
        del first_num[0]
        del second_num[0]
        in_mind = digit_1

# for el in max(first_num, second_num):
#     sum_num = el + in_mind
#     digit_1 = sum_num // 10
#     digit_2 = sum_num % 10

    # result_num.append(digit_2 + in_mind)
    # in_mind = digit_1

result_num = [str(x) for x in result_num]
print(' '.join(result_num))
