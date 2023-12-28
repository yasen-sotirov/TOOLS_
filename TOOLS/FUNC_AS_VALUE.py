"ПРИНЦИПИ ОТ ФУНКЦИОНАЛНОТО ПРОГРАМИРАНЕ"   # постигаме високо ниво на абстракност и гъвкавост









"ФУНКЦИЯ КАТО ПРОМЕНЛИВА"
# variable_1 = print
# variable_1("Hi you")



"ФУНКЦИЯ С ПАРАМЕТЪР ДРУГА ФУНКЦИЯ - Python Closures"
# def greet(name):
#     def display_name():
#         print("Hi", name)
#     display_name()
#
# greet("John")



# from math import sqrt
# def apply_func(input_func, num):
#     return input_func(num)
#
# print(apply_func(abs, -5))
# print(apply_func(float, 5))
# print(apply_func(sqrt, 121))



# def add_text():
#     output = ""
#     def append_func(word: str):
#         nonlocal output
#         output += word.capitalize()
#         return output
#     return append_func
#
# # понеже пазим в променлива се получава натрупване на Бла
# result = add_text()
# print(result("bla"))
# print(result("bla"))
#
# # викаме вложената функция
# # не пазим в променлива, затова няма натрупване
# print(add_text()("bla"))
# print(add_text()("bla"))






"HIGH ORDER FUNCTION"



"СОЧИ НА ЕДНО И СЪЩО МЯСТО В ПАМЕТТА"
# my_print = print
# print(my_print)
# print(print)