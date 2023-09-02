"РЕКУРСИЯ"   # да ревърснеш стринг рекурсивно
#  линейни и с разклинения



"ПРОМЕНЯ БРОЯ РЕКУРСИИ"
# import sys
# sys.setrecursionlimit(10000)


"ФАКТОРИЕЛ"
"""
n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 1
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!

уравненията не са завършени, защото в тях има нещо неизвестно
когато стигне дъното вижда това неизвестно и го подава на предходното
чакащо уравнение, което вече може да бъде сметнато. Като го пресметне,
вече има резултат, който да помогне за завършавнето на предходното
уравнение. И така до началото.
"""
# def factorial_rec(num):
#     if num <= 1:
#         return 1
#     return num * factorial_rec(num - 1)
#
# print(factorial_rec(5))

# 120
# factorial_rec(5)
# return 5 * factorial_rec(4)
#            return 4 * factorial_rec(3)
#                       return 3 * factorial_rec(2)
#                                  return 2 * factorial_rec(1)
#                                             return 1




"МНОЖЕСТВЕНА РЕКУРСИЯ  - ЕЛФИ И ДОСТАВКИ"
def deliver_present(kids_list):
    if len(kids_list) == 1:
        print(f"Deliver present to: {kids_list[0]}")
    else:
        mid = len(kids_list) // 2
        first_half = kids_list[:mid]
        second_half = kids_list[mid:]

        # елф едно
        deliver_present(first_half)
        # елф две
        deliver_present(second_half)

child = ["Ivan", "Pesho", "Tosho", "Gosho", "Ginka", "Stamat", "Gertruda", "Kalinka"]
deliver_present(child)



"ПРИМЕРИ"       # ако сложим принта вътре ще смени реда
# def print_num(max_num):
#     # условие/дъно
#     if max_num == 0:
#         return
#
#     # ако не е дъно, прави следното
#     print_num(max_num - 1)
#     print(max_num)
#
# print_num(5)



# def print_num(max_num):
#     if max_num != 0:
#         print_num(max_num - 1)
#         print(max_num)
#
# print_num(5)




"STRING REVERSE"
"""
ози код представлява функция, която обръща подаден низ използвайки рекурсия. Да разгледаме как работи по стъпки:

    Функцията reverse_recursive(string) приема низ като входен аргумент.
    Първо проверява дали низът string е празен (дъно на рекурсията). Ако е празен, тя връща празен низ '', терминирайки изпълнението на рекурсията.
    В противен случай (когато низът string не е празен), тя взима последния символ от низа чрез string[-1] и го записва в променливата last.
    След това връща конкатенацията на last (последния символ) с рекурсивното извикване на същата функция, но със срязан низ без последния символ: reverse_recursive(string[:-1]).
    Така рекурсията продължава, като се връщат символите в обратен ред, като последния символ на първата рекурсивна стъпка става първи в резултата, втория става втори и така нататък.
    Рекурсията продължава докато низът стане празен, като всяка стъпка добавя последния символ към текущия резултат.

Примерно изпълнение с низа "abc":

    string не е празен, затова премахваме последния символ и го записваме в last (last = 'c').

    Връщаме 'c' + reverse_recursive('ab').

    Рекурсия за 'ab':

        string не е празен, затова премахваме последния символ и го записваме в last (last = 'b').

        Връщаме 'b' + reverse_recursive('a').

        Рекурсия за 'a':

            string не е празен, затова премахваме последния символ и го записваме в last (last = 'a').

            Връщаме 'a' + reverse_recursive('').

            Рекурсия за '':
                string е празен, връщаме празен низ ''.

        В рекурсията за 'a' получаваме резултат 'a' + '', което е просто 'a'.

    В рекурсията за 'ab' получаваме резултат 'b' + 'a', което е 'ba'.

В рекурсията за 'abc' получаваме резултат 'c' + 'ba', което е 'cba'.

Така се получава желаният обратен низ 'cba' за входния низ 'abc'.
"""
# def reverse_recursive(string):
#     if string == "":
#         return ''
#
#     last_el_list = string[-1]
#     return  last_el_list + reverse_recursive(string[:-1])
#
# print(reverse_recursive("abc"))

# 'abcd' -> 'dcba'
# 'd' + 'cba'
#       // 'c' + 'ba'
#              // 'b' + 'a'
#                     // 'a' = reverse('')



# =========================
# def reverse_recursive(s):
#     if s == "":
#         return ''
#     return reverse_recursive(s[1:]) + s[0]
#
# the_result = reverse_recursive("abc")
# print(the_result)




"FLATTEN ИЗРАВНЯВАНЕ" # рекурсия с разклонения
def flatten(lst):
    output = []
    # проверява дали елемента е число или списък
    for el in lst:
        if isinstance(el, int):
            output.append(el)
        else:
            # ако е събсписък разширява текущия списък с резултата от вложения списък
            output.extend(flatten(el))
    return output

values = [1, 2, [[[3, [4, [5, [6]]]], 7], 8, 9]]
print(flatten(values))




"ЛАБИРИНТ"      # рекурсия с 4 разклоненя
# lab = [
#     [1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0]
# ]
#
# rows = len(lab)
# cols = len(lab[0])
#
# # 0,0  1,0  1,1  1,2  2,2  3,2  3,1
#
# for r in range(rows):
#     for c in range(cols):
#         if lab[r][c] == 1:
#             print(r,c)



"FIBONACCI С ОПТИМИЗАЦИЯ"   # F(n) = F(n-1) + F(n-2)
# създава кеш, където пази калкулираните стойности и когато
# потрябват ги взема от там, а не ги смята отново
# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibo_opty(num):
#     print("fibonacci recursive with n = ", num)
#
#     if num <= 2:
#         return 1
#     return fibo_opty(num-1) + fibo_opty(num-2)
#
# print("Result = ", fibo_opty(100))




"ПАЗИ РЕЗУЛТАТИТЕ В DICT"   # memoization
# https://learn.telerikacademy.com/mod/page/view.php?id=50290

# def fibonacci_m(n, memo={}):
#     base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#
#     if n in memo:
#         return memo[n]
#
#     nth_fibo = (fibonacci_m(n - 1, memo) + fibonacci_m(n - 2, memo))
#
#     memo[n] = nth_fibo
#     return nth_fibo
#
# print(fibonacci_m(5))




"ОПТИМИЗАЦИЯ ПРИ РАБОТА С ЛИСТОВЕ"
# # прави се така:
# def sum_list(lst):
#     def helper(start_index):
#         if start_index == len(lst):
#             return 0
#         return lst[start_index] + helper(start_index + 1)
#     return helper(0)
#
# # а не така, защото всеки път ще прави копие на листа, което товари
# def sum_lst(lst):
#     if lst == []:
#         return 0
#     return lst[0] + sum_lst(lst[1:])




" ======== CODING TASKS ======== "

# === 1: Factorial
"""
Given n of 1 or more, return the factorial of n, 
which is n * (n-1) * (n-2) ... 1. 
Compute the result recursively (without loops).

On the first line you will be given n.

On the only output line you should print F(n).
Constraints n>1

Input
1
1

Input
5

120
"""
# def factorial_rec(num):
#     if num <= 1:
#         return 1
#     return num * factorial_rec(num - 1)
#
# num = int(input())
# print(factorial_rec(num))


# === 2: Bunny Ears
"""
Bunny Ears
We have a number of bunnies and each bunny has two big floppy ears. 
We want to compute the total number of ears across all the bunnies 
recursively (without loops or multiplication).
"""
# def bunny_ears(bunny):
#     if bunny == 0:
#         return 0
#     if bunny == 1:
#         return 2
#     return 2 + bunny_ears(bunny -  1)
#
# data = int(input())
# print(bunny_ears(data))




# === 3: Fibonacci
"""
Fibonacci
The Fibonacci sequence is a famous bit of mathematics, 
and it happens to have a recursive definition. The first two values in 
the sequence are 0 and 1 (essentially 2 base cases). 
Each subsequent value is the sum of the previous two values, 
so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. 
Define a recursive fibonacci(n) method that returns the nth 
Fibonacci number, with n=0 representing the start of the sequence.
"""
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
# =======================================

# def fib(n, memo={0: 0, 1: 1, 2: 1}):
#     if n in memo:
#         return memo[n]
#     memo[n] = fib(n - 2) + fib(n - 1)
#     return memo[n]
#
# print(fib(int(input())))



# === 4 Bunny ears 2
"""
We have bunnies standing in a line, numbered 1, 2, ... 
The odd bunnies (1, 3, ..) have the normal 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears, because they each 
have a raised foot. Recursively return the number of "ears" in the bunny 
line 1, 2, ... n (without loops or multiplication).
"""
# def bunny_ears(bunny):
#     if bunny == 0:
#         return 0
#     if bunny == 1:
#         return 2
#     return 5 + bunny_ears(bunny -  2)
#
# data = int(input())
# print(bunny_ears(data))
# ==========================================
# def bunny_ears(n):
#     return (3 if n % 2 == 0 else 2) + bunny_ears(n - 1) if n > 0 else 0
# print(bunny_ears(int(input())))




# === 5 Triangle
"""
We have triangle made of blocks. The topmost row has 1 block, 
the next row down has 2 blocks, the next row has 3 blocks, and so on. 
Compute recursively (no loops or multiplication) the total number of 
blocks in such a triangle with the given number of rows."""
# def triangle_of_blocks(rows):
#     if rows == 0:
#         return 0
#     if rows == 1:
#         return 1
#     return rows + triangle_of_blocks(rows - 1)
#
# data = int(input())
# print(triangle_of_blocks(data))
# =================================================
# def triangle(n):
#     return n + triangle(n - 1) if n > 0 else 0
# print(triangle(int(input())))





# === 6: Sum Digits
"""
Write a program that reads a four-digit number 
and displays the sum of its digits
"""
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
# ================================================
# def sum_digits(n):
#     head, *tail = n
#     return head + (sum_digits(tail) if tail else 0)
# print(sum_digits(map(int, list(input()))))





# === 7: Count occurrences
"""
Given a non-negative int n, return the count of the occurrences of 7 
as a digit, so for example 717 yields 2. (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""
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
# =========================================
# def count_sevens(n):
#     head, *tail = n
#     # parse True to 1 and False to 0
#     return int(head == '7') + (count_sevens(tail) if tail else 0)
# print(count_sevens(list(input())))





# === 8: Count occurrences 2 TODO
"""
Given a non-negative int n, compute recursively (no loops) 
the count of the occurrences of 8 as a digit, except that an 8 with 
another 8 immediately to its left counts double, so 8818 yields 4.

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""
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
# =====================================================
# def count_eights(n):
#     if not n:
#         return 0
#     first, *tail = n
#     if not tail:
#         return int(first == '8')
#     if first == '8' and tail[0] == '8':
#         return 2 + count_eights(tail)
#     if first == '8':
#         return 1 + count_eights(tail)
#     return count_eights(tail)
# print(count_eights(list(input())))







# === 9: Power N
"""
Given base and n that are both 1 or more, compute recursively (no loops)
the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
"""
# def power_n(base, power):
#     if power == 0:
#         return 1
#     return base * power_n(base, power - 1)
#
# base = int(input())
# power = int(input())
# print(power_n(base, power))
# =======================================
# def power(n, p):
#     return n * (power(n, p - 1) if p > 1 else 1)
# print(power(int(input()), int(input())))





# === 10 Count X
"""
Given a string, compute recursively (no loops) the number of 
lowercase 'x' chars in the string.
"""
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
# ============================================
# def count_x(s):
#     head, *tail = s
#     return int(head == 'x') + (count_x(tail) if tail else 0)
# print(count_x(list(input())))





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
# ================================
# def count_hi(s):
#     if len(s) < 2:
#         return 0
#     return int(s[0:2] == 'hi') + count_hi(s[1:])
# print(count_hi(input()))





# === 12: Change Pi
"""
Given a string, compute recursively (no loops) a new string
where all appearances of "pi" have been replaced by "3.14".
"""
# def change_pi(string):
#     if len(string) < 2:
#         return string
#
#     # ако стрингът от инд 0 до инд 2 ексклузив е = pi
#     if string[:2] == "pi":
#         # върни 3,14 + остатъка от стринга [от 2 вкл.: нататък]
#         return "3.14" + change_pi(string[2:])
#     else:
#         # ако не е, върни стр на инд.0 + стр от инд.1 нататък
#         # тук преминава на следващия елемент от стринга
#         return string[0] + change_pi(string[1:])
#
# data = input()
# print(change_pi(data))
# ================================
# def change_pi(s):
#     if len(s) < 2:
#         return s
#     if s[0:2] == 'pi':
#         return '3.14' + change_pi(s[2:])
#     return s[0] + change_pi(s[1:])
# print(change_pi(input()))




# === 13: Array with 6
"""
Given an array of ints, compute recursively if the array contains a 6.
We'll use the convention of considering only the part of the array
that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass in
index as 0.
1,6,4
0

1

1,4,6,2,6,1,6
3

2
"""
# def array_with_six(arr, idx):
#     arr = arr[idx:]
#     if arr == []:
#         return "false"
#     if arr[0] == 6:
#         return "true"
#     return array_with_six(arr[1:], 0)
#
# array = [int(el) for el in input().split(",")]
# start_idx = int(input())
# print(array_with_six(array, start_idx))
# ===============================================
# def has_six(arr):
#     if not arr: return False
#     return arr[0] == '6' or has_six(arr[1:])
# result = has_six(input().split(',')[int(input()):])
# print(str(result).lower())




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
# =============================================
# def count_elevens(arr):
#     if not arr: return 0
#     return int(arr[0] == '11') + count_elevens(arr[1:])
# print(count_elevens(input().split(',')[int(input()):]))






# === 15: Array values times 10
""" 
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
# ===========================================
# def count_values_times_10(lst):
#     if len(lst) < 2:
#         return False
#     if lst[0] * 10 == lst[1]:
#         return True
#     return count_values_times_10(lst[1:])
# result = count_values_times_10(list(map(int, input().split(',')[int(input()):])))
# print(str(result).lower())

