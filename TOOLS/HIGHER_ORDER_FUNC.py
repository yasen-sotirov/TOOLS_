"HIGHER ORDER and ANONYMOUS"   # https://www.kite.com/blog/python/functional-programming/
# map() и filter() създават обект който се изтощава
# затова може да ги конвертираме към лист

# функциите могат да бъдат запазвани като стойности или референции
# функционално програмиране - функциите могат да бъдат комбинирани групирани и др
# в Питон можем да третираме функциите като стойности


"ЛАМБДА"
# анонимна функция, ползва се само на едно място в кода
# синтаксис:    lambda аргумент: израз на един ред


number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
number_list_2 = [4, 8, 2, 6, 9]
number_list_3 = [1, 2, 3, 4, 5]
letters_list = ['cat', 'dog', 'mouse', 'hello', 'world']


"ФИЛТРИРАНЕ НА LIST С LAMBDA"
# print(list(filter(lambda x: x % 2 == 0, number_list)))
# print(list(filter(lambda x: len(x) >= 4, letters_list)))
#
# print(list(map(lambda num: num ** 2, number_list)))                 # функция за прилагане, върху лист
# print(list(map(lambda x, y: x*y, number_list_2, number_list_3)))    # умножава елементите от първия списък с елементите от втория списък
#
# measurement = [ {'length': 2.5, 'width': 2},
#                 {'length': 3, 'width': 6},
#                 {'length': 5, 'width': 4}]
# print(list(map(lambda x: x.get('length', 0) * x.get('width', 0), measurement)))



"СОРТИРАНЕ НА LIST С LAMBDA"
# dict_list = {"ABCC": 4, "CABB": 7, "ABB": 3, "BB": 5, "AB": 2, "AABBB": 1, "BBC": 6, "CBA": 8, "ACA": 9, "CBC": 10}
#
# print(sorted(dict_list, key=lambda x: x, reverse=True))   # намалява по първа буква, лексикографски
# print(sorted(dict_list, key=lambda x: x))                 # нараства по първа буква
# print(sorted(dict_list, key=lambda x: (x[0], x[1])))      # нараства по първа и втора буква
# print(sorted(dict_list, key=lambda x: x[1]))              # нараства по втора буква
# print(sorted(dict_list, key=lambda x: len(x)))            # нараства по дължина
# print(sorted(dict_list, key=lambda x: (x, len(x))))       # нараства по първа буква и по дължина
# print(sorted(dict_list, key=lambda x: dict_list[x]))      # нараства по стойностите на value





"MAP"
# минава през колекция като трансформира стойностите ѝ
# като за целта използва друга функция
# може да се направи и с list comprehension

# def double_num(number):
#     if number % 2 == 0:
#         return number * 2
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# result = map(double_num, lst)
# print(list(result))         # list() иначе връща <#object>

# names = ['iVan', 'blagoi', 'geORgi', 'LENA']
# print(list(map(str.capitalize, names)))


"ЧЕТЕНЕ ОТ INPUT C MAP"
input  = 'shoot 2 3'
rows, cols = map(int, input().split()[1:])
print(f"row: {rows}, col: {cols}")



"FILTER"    # връща елементите, които отговарят на филтъра
# numbers = ['12', 'ab', '6', 'cd']
# print(list(filter(str.isdigit, numbers)))   # list() иначе връща <#object>



"HIGHER ORDER ФУНКЦИИ"
#  всяка една функция, която като входни данни приема друга функция
#  или създава функция и връща референция към нея

# def multiply_by_two(func, x):
#     result = func(x)
#     return result * 2
#
# def add_five(y):
#     return y + 5
#
# print(multiply_by_two(add_five, 3))     # (3 + 5) * 2 = 16




"ФУНКЦИЯ КАТО СТОЙНОСТ"
# for p in [print] * 10:
#     p('Hi')







#
#
#
#
#
#
# "REDUCE"
# from functools import reduce
#
# # 1. Return the product of an list of numbers.
# multiply_num = [1, 2, 3, 4, 5]
# print(reduce(lambda num_1, num_2: num_1 * num_2, multiply_num))
#
# # 2. Return the maximum number in a list of numbers.
# # Hint: with reduce you can also replace the result of the previous iteration.
# max_list = [7, 13, 72, 14]
# print(reduce(lambda x, y: x if x > y else y, max_list))
#
#
# # 3. Return the longest string in a list of strings.
# long_list = ['cat', 'dog', 'elephant', 'cucumber']
# print(reduce(lambda w1, w2: w2 if len(w1) > len(w2) else w2, long_list))
#
#
# # 4. Reverse a string. Hint: A string is just a list of characters.
# # To use reduce on a string, you can spread it a list like this: [...'apple'].reduce(...
#
#
#
# from functools import reduce
#
# number_list = [1, 2, 4, 5, 6, 11, 9, 8]
#
# def get_even(num):
#     return num % 2 == 0
#
# result = list(filter(get_even, number_list))
# print(result)
#
#
# result_lambda = list(filter(lambda num: num % 2 == 0, number_list))
# print(result_lambda)
#
#
# line = ["abc", "1", "2.5", "5"]
# numbers = list(filter(lambda num: num.isnumeric(), line))
#
# # само int   num.isdgit()
# # numbers.isallnum()
# # number.isdecimal()
# # numbers.is digit
# # number.
#
#
# print(reduce(lambda x, y: x + y, number_list))
