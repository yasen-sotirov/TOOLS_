"ФУНКЦИИ"       # за да приключи функцията трябва да имаме return
                # задължителните, наименованите, args, kwargs
                # променлива, която е дефинирана във функция не е видима извън нея
                # лекция с Инес Иванова  https://softuni.bg/trainings/resources/video/61350/video-09-june-2021-ines-ivanova-python-fundamentals-may-2021/3368

# Параметъ = променливите, с които работи функцията
# Аргумент = променливите, които подаваме на функцията
# позиционни аргументи - ненаименовани аргументи
# теория   https://www.tutorialaicsip.com/cs-xii-qna/working-with-functions-class-12/


" (*, ...) СЛЕД НЕЯ ЗАДЪЛЖИТЕЛНО СЛЕДВАТ KEY-WORD ARGUMENTS"


"ОПАКОВАНЕ В ЛИСТ *ARGS"        # поема неограничен брой аргументи и ги опакова в масив
# def print_nums_funct(*args):
#     for el in args:
#         print(el)
#
# nums_1 = 1
# nums_2 = 2
# nums_3 = 3
# print_nums_funct(nums_1, nums_2, nums_3)

# def funct(*, a, b):
#     print(True)
#
# funct(a=1, b=2)
# аргументите след звездата трябва да са описани
# като key-word аргументи „а=“



"РАЗОПАКОВАНЕ НА ЛИСТ"
# разопакова листа и го подава на функцията
# def print_nums(a, b, c):
#     print(a, b, c)
# nums = [1, 2, 3]
# print_nums(*nums)

# def even_odd(*args):
#     *numbers, command = args
#     party = 0 if command == "even" else 1
#     return [el for el in numbers if el % 2 == party]
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))





"**KVARGS"  # key-word args, поема неограничен бр наименувани елементи
# def info_functtion(**kwargs):                     # ОПАКОВА В РЕЧНИК
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} " \
#            f"and he is {kwargs.get('age')} years old"
#
# print(info_functtion(**{"name": "George", "town": "Sofia", "age": 20}))  # РАЗОПАКОВА РЕЧНИК И ГО ПОДАВА КАТО ПАРАМЕТЪР
# print(info_functtion(name="George", town="Sofia", age=20))



"ДОБАВЯНЕ МАХАНЕ И ДР. ОТ **KWARGS"  # работи със всички методи на речници дето си знаем
# def info_functtion(**kwargs):
#     kwargs["example"] = 123
#     print(kwargs)
#     del kwargs["name"]
#     print(kwargs)
#
# info_functtion(**{"name": "George", "town": "Sofia", "age": 20})



"ИТЕРИРАНЕ ПРЕЗ **KWARGS"
# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{value}, {key}")
#
# greet_me(Peter="Hello", George="Bye")



"ВКЛЮЧВАНЕ НА РЕЧНИЦИ И ДРУГИ"
# def example_func(nums, dict, *args, **kwargs):
#
#     print(example_func([1, 2, 3], {"a": 1, "b": 2}, 1, 2, 3, name="Test"))




"ОБЕДИНЯВА *ARGS"
# def concatenate(*args):
#     return ''.join(args)
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!"))



"ПОКАЗBА ДОКУМЕНТАЦИШТА ЗА ДАДЕНА ФУНКЦИШ"
# def example_func():
#     """This function just say Hello"""
#     return "Hello"
# print(example_func.__doc__)






"БРОЙ ЕЛЕМЕНТИТЕ НА ФУНКЦИЯТА"
# def custom_reduce(func, elements):
#     argument_count = func.__code__.co_argcount
#     print(argument_count)
#
# print(custom_reduce(lambda a, b: a + b, [1, 2, 3]))


"CUSTOM REDUCE"
# from collections import deque
# def custom_reduce(func, elements):
#     elements = deque(elements)
#
#     argument_count = func.__code__.co_argcount
#     while len(elements) > 1:
#         argument = [elements.popleft() for _ in range(argument_count)]
#         elements.appendleft(func(*argument))
#     return elements[0]
# print(custom_reduce(lambda a, b: a + b, [1, 2, 3, 1, 2, 3]))


# List of Tuples Declaration
# planets = [("Earth", 3),("Jupiter",5),("Mercury",1), ("Mars",4), ("Neptune",8), ("Saturn", 6), ("Uranus",7), ("Venus",2)]
# print(planets)
#
# new_list = sorted(planets, key=lambda x: x[1], reverse=True)
# print("Sorted List: {new_list}")
# print("original List: ", planets)
#
# # Sorts the list by the item value of the second element of the Tuple
# SelectPlanets = sorted(planets, key = lambda x : x[1])
#
# print(SelectPlanets)





# list_1 = [4, 2, 13, 21, 5]
# final_list = []
#
# for i in list_1:
#     temp = lambda i: i ** 2
#     final_list.append(temp(i))
#
# print(final_list)





"МАП"
# def double_num(number):
#     if number % 2 == 0:
#         return number * 2
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# result = map(double_num, num_list)
# print(list(result))



"CONTINUE"  # АКО ВЛЕЗЕ В IF ЩЕ ПРОПУСНЕ НАСТОЯЩИЯ ЦИКЪЛ
# i = 0
# while i < 9:
#     i += 1
#     if i == 3:
#         continue
#     print(i)



"BREAK"  # АКО ВЛЕЗЕ В IF ЩЕ ПРЕКЪСНЕ ЦЕЛИЯ WHILE
# i = 0
# while i < 9:
#     i += 1
#     if i == 3:
#         break
#     print(i)




"ФУНКЦИЯ ОТ СТРИНГ"
# expression = "(5+2*4)/2"
# result = eval(expression)
# print(result)