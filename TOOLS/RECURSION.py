"РЕКУРСИЯ"   # да ревърснеш стринг рекурсивно
#  линейни и с разклинения



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
# def deliver_present(kids_list):
#     if len(kids_list) == 1:
#         print(f"Deliver present to: {kids_list[0]}")
#     else:
#         mid = len(kids_list) // 2
#         first_half = kids_list[:mid]
#         second_half = kids_list[mid:]
#
#         # елф едно
#         deliver_present(first_half)
#         # елф две
#         deliver_present(second_half)
#
# child = ["Ivan", "Pesho", "Tosho", "Gosho", "Ginka", "Stamat", "Gertruda", "Kalinka"]
# deliver_present(child)



"ПРИМЕРИ"       # ако сложим принта вътре ще смени реда
def print_num(max_num):
    # условие/дъно
    if max_num == 0:
        return

    # ако не е дъно, прави следното
    print_num(max_num - 1)
    print(max_num)

print_num(5)



# def print_num(max_num):
#     if max_num != 0:
#         print_num(max_num - 1)
#         print(max_num)
#
# print_num(5)




"STRING REVERSE"
# "abcdef" -> "fedcba"
def reverse_recursive(string):
    if string == "":
        return ''

    last = string[-1]
    return  last + reverse_recursive(string[:-1])

reverse_recursive("abc")
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
# values = [1, [2, [[[3, [4, [5, [6]]]], 7], 8], 9]]
#
# def flatten(lst):
#     output = []
#     for x in lst:
#         if isinstance(x, int):
#             output.append(x)
#         else:
#             output.extend(flatten(x))
#     return output
#
# values2 = flatten(values)
# print(values2)




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