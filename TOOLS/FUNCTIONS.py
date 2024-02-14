"ФУНКЦИИ"       # за да приключи функцията трябва да имаме return
                # задължителните, наименованите, args, kwargs
                # променлива, която е дефинирана във функция не е видима извън нея
                # лекция с Инес Иванова  https://softuni.bg/trainings/resources/video/61350/video-09-june-2021-ines-ivanova-python-fundamentals-may-2021/3368

# Параметър = променливите, с които дефинираме функцията
# Аргумент = променливите, които подаваме когато извикваме функцията
# позиционни аргументи - ненаименовани аргументи
# теория   https://www.tutorialaicsip.com/cs-xii-qna/working-with-functions-class-12/


" (*, ...) СЛЕД НЕЯ ЗАДЪЛЖИТЕЛНО СЛЕДВАТ KEY-WORD ARGUMENTS"
# def funct1(a, *, b, c):
#     print(a, b, c)
# funct1(1, b=2, c=3)     # print без скоби
#
# def funct2(a, *, b, c):
#     return a, b, c
# print(funct2(1, b=2, c=3))      # print със скоби


" (..., /) ПРЕДИ НЕГО ЗАДЪЛЖИТЕЛНО ИМА KEY-WORD ARGUMENTS"
# def func(x, /, y):      # прави един параметър преди него linear parameter
#     return x, y
# print(func(5, 6))



"ОПАКОВАНЕ В ЛИСТ *ARGS"
# събира множество подадени аргументи в тюпъл и ги подава на функцията.
# def print_nums_funct(*args):
#     print(type(args))
#     for el in args:
#         print(el * 2)
# nums_1, nums_2, nums_3 = 1, 2, 3
# print_nums_funct(nums_1, nums_2, nums_3)
#
# def concatenate(*args):
#     return ''.join(args)
# print(concatenate("Soft", "UNI", "Is", "Grate", "!"))




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
# def info_function(**kwargs):                     # ОПАКОВА В РЕЧНИК
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} " \
#            f"and he is {kwargs.get('age')} years old"
#
# print(info_function(**{"name": "George", "town": "Sofia", "age": 20}))  # РАЗОПАКОВА РЕЧНИК И ГО ПОДАВА КАТО ПАРАМЕТЪР
# print(info_function(name="George", town="Sofia", age=20))


"CONTINUE"  # АКО ВЛЕЗЕ В IF ЩЕ ПРОПУСНЕ НАСТОЯЩИЯ ЦИКЪЛ
# i = 0
# while i < 9:
#     i += 1
#     if i == 3:
#         continue
#     print(i)



"BREAK"  # АКО ВЛЕЗЕ В IF ЩЕ ПРЕКЪСНЕ ЦЕЛИЯ ЦИКЪЛ
# i = 0
# while i < 9:
#     i += 1
#     if i == 3:
#         break
#     print(i)



"ВРЪЩА ДОКУМЕНТАЦИЯТА НА ДАДЕНА ФУНКЦИЯ"
# def example_function_for_documentation_preview_and_alias(text: str):
#     """This function just say Hello"""
#     return text
#
# func = example_function_for_documentation_preview_and_alias("Hello")
# print(func)
# print(func.__doc__)




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




"ФУНКЦИЯ ОТ СТРИНГ: evaluation"
# expression = "(5+2*4)/2"
# result = eval(expression)
# print(result)



"ИЗПИСВАНЕ НА return НА ДВА РЕДА"
# def second_line_return(line_1, line_2):
#     return f'str: {line_1}' \
#            f'str: {line_2}'
#
# print(second_line_return('text_1', 'text_2'))