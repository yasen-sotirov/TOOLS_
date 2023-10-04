# === 1      5! = 5*4*3*2*1 = 120
# def factorial_rec(num):
#     if num <= 1:
#         return 1
#     return num * factorial_rec(num - 1)
#
# num = int(input())
# print(factorial_rec(num))


# === 2 Bunny Ears
# def bunny_ears(bunny):
#     if bunny == 0:
#         return 0
#     if bunny == 1:
#         return 2
#     return 2 + bunny_ears(bunny -  1)
#
# data = int(input())
# print(bunny_ears(data))


# === 3
# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# num = int(input())
# print(fibonacci(num))



# === 4 Bunny ears 2
# def bunny_ears(bunny):
#     if bunny == 0:
#         return 0
#     if bunny == 1:
#         return 2
#     return 5 + bunny_ears(bunny -  2)
#
# data = int(input())
# print(bunny_ears(data))



# === 5 Triangle
# def triangle_of_blocks(rows):
#     if rows == 0:
#         return 0
#     if rows == 1:
#         return 1
#     return rows + triangle_of_blocks(rows - 1)
#
# data = int(input())
# print(triangle_of_blocks(data))



# === 6 Sum Digits
# def sum_digits(digit: list[int]):
#     def helper(start_index):
#         # ако списъка е = 0, значи е празен и връща нула
#         if start_index == len(digit):
#             return 0
#         # започва да събира 0 индекс със следващите индекси
#         # като ги повдига с 1
#         return digit[start_index] + helper(start_index + 1)
#     # задаваме индекса да е 0
#     return helper(0)
#
# data = [int(el) for el in input()]
# print(sum_digits(data))



# === 7 Count occurrences
# def count_occurrences(number):
#     if number == 0:
#         return 0
#
#     elif number % 10 == 7:
#         return 1 + count_occurrences(number // 10)
#     else:
#         return count_occurrences(number // 10)
#
# num = int(input())
# print(count_occurrences(num))



# === 8 Count occurrences 2 TODO
# def count_occurrences(number):
#     if number == 0:
#         return 0
#
#     elif number // 10 == 8 and number % 10 == 8:
#         return 2 + count_occurrences(number // 10)
#     elif number % 10 == 8:
#         return 1 + count_occurrences(number // 10)
#     else:
#         return count_occurrences(number // 10)
#
# num = int(input())
# print(count_occurrences(num))


# === 9 Power N
# def power_n(base, power):
#     if power == 0:
#         return 1
#     return base * power_n(base, power - 1)
#
# base = int(input())
# power = int(input())
# print(power_n(base, power))



# === 10 Count X
# def change_pi(string):
#     # достигам дъното, когато свърши стринга
#     # тогава връщам 0, която се закача към калкулацията
#     if string == "":
#         return 0
#
#     else:
#         if string[0] == "x":
#             # ще одреже първия елемент от стринга
#             # ще добави единица към сбора, който се натрупва
#             return 1 + change_pi(string[1:])
#         else:
#             # ще одреже първия елемент от стринга
#             return change_pi(string[1:])
#
# data = input()
# print(change_pi(data))


# === 11 Count hi
"""
Given a string, compute recursively (no loops) the number of times
lowercase "hi" appears in the string.
On the first line you will be given the string.
On the only output line you should print the number of hi-s.

xxhixx
1

xhixhix
2
"""
# def count_x(string):
#     # стрингът трябва да има дължина мин 2 елемента
#     if len(string) < 2:
#         return 0
#
#     if string[:2] == "hi":
#         return 1 + count_x(string[2:])
#     return count_x(string[1:])
#
# data = input()
# print(count_x(data))



# === 12: Change Pi
# Given a string, compute recursively (no loops) a new string
# where all appearances of "pi" have been replaced by "3.14".

def change_pi(string):
    if len(string) < 2:
        return string

    # ако стрингът от инд 0 до инд 2 ексклузив е = pi
    if string[:2] == "pi":
        # върни 3,14 + остатъка от стринга [от 2 вкл.: нататък]
        return "3.14" + change_pi(string[2:])
    else:
        # ако не е, върни стр на инд.0 + стр от инд.1 нататък
        # тук преминава на следващия елемент от стринга
        return string[0] + change_pi(string[1:])

data = input()
print(change_pi(data))




# === 13: Array with 6
"""
Given an array of ints, compute recursively if the array contains a 6.
We'll use the convention of considering only the part of the array
that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass in
index as 0.
1,6,4
0

1,4
0
"""
# def array_with_six(arr, idx):
#     arr = arr[idx:]
#     if arr == []:
#         return "false"
#
#     if arr[0] == 6:
#         return "true"
#     return array_with_six(arr[1:], 0)
#
# array = [int(el) for el in input().split(",")]
# start_idx = int(input())
# print(array_with_six(array, start_idx))



# === 14: Arrays containing 11
"""Given an array of ints, compute recursively the number of times
that the value 11 appears in the array.
We'll use the convention of considering only the part of the array
that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass
in index as 0.
On the first line you will be given the comma separated array.
On the second line you will receive the index.
1,2,11
0

11,11
0
"""
# def containing_11(lst, idx):
#     lst = lst[idx:]
#     if lst == []:
#         return 0
#
#     else:
#         if lst[0] == 11:
#             return 1 + containing_11(lst[1:], 0)
#         else:
#             return containing_11(lst[1:], 0)
#
# data = [int(el) for el in input().split(",")]
# index = int(input())
# print(containing_11(data, index))

""" # === 15: Array values times 10
Given an array of ints, compute recursively if the array contains 
somewhere a value followed in the array by that value times 10.
We'll use the convention of considering only the part of the array that 
begins at the given index. In this way, a recursive call can pass 
index+1 to move down the array. The initial call will pass in index as 0.

On the first line you will be given the comma separated array. 
On the second line you will receive the index.

On the only output line you should print the result.

1,2,20
0       -> true

3,30
0       -> true
"""
# def array_value(array, ind):
#     array = array[ind:]
#     if len(array) == 1 or ind > len(array) + 2:
#         return "false"
#
#     if array[1] % array[0] == 0:
#         return "true"
#     return array_value(array[1:], 0)
#
# data = [int(el) for el in input().split(",")]
# index = int(input())
# print(array_value(data, index))


