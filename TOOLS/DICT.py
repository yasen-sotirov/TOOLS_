"DICTIONARIES"      # Abstract Data Structure
# eys - immutable - ключовете са уникални
# values - mutable - променлив. може да се добавя променя ...
# референтен тип данни
# скоростта на търсене в речник е О1


classes = {'1A': ["Ines", "Pesho"], '1B': ["Ivan", "Maria"]}   # един ключ може да садържа множество велюта
students = {'№1': {'name': 'Pesho', 'ages': 12}, '№2': {'name': 'Ivan', 'ages': 11}}
my_dict = {'a': 25, 'b': "Pesho", 2: 33}
num_dict = {'a': 1, 'b': 2, 'c': 3}
num_dict_2 = {1: 6, 2: 5, 3: 14}
letter_dict = {'A': 4, 'C': 3, 'B': 1, 'D': 2}
names_ages = {"Ines": 27,
              "Georgi": 43,
              "Pesho": 40,
              "Marieta": 37,
              "Maria": 52}      # така е по PEP стандарт


"ДОБАВЯНЕ В РЕЧНИКА"
# print(my_dict)
# my_dict["eyes color"] = "green"
# print(my_dict)

# print(classes)
# classes["1A"].append("New name")    # при валю списък
# print(classes)


# print(classes)
# new_class = '1C'
# new_student = 'Blagoi'
# if new_class not in classes:
#     classes[new_class] = []
# classes[new_class].append(new_student)
# print(classes)



"ПРОМЯНА В РЕЧНИКА"
# print(my_dict)
# my_dict[2] = 66
# print(my_dict)

# print(classes)
# classes['1A'][1] = "Yasen"
# print(classes)



"ТЪРСЕНЕ В РЕЧНИК"
# directions = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0)}
#
# def get_direction(move):
#     if move in directions:
#         return directions[move]
# print(get_direction("left"))
#
# # търси в ключа
# print("a" in num_dict)  # True
# print("f" in num_dict)  # False
#
# # търси в value
# print(3 in num_dict.values())  # True



"ПРЕМАХВА K-V ДВОЙКА"
# print(my_dict)
# del my_dict[2]
# print(my_dict)

# print(my_dict)
# key = my_dict.pop("b")      # вади по ключ, или последната ако не запишем нищо в скобите
# print(my_dict)
# print('The key is: ', key)

# print(my_dict)
# kvpt = my_dict.popitem()     # трие последната двойка и пази като тюпъл
# print(my_dict)
# print(kvpt)
# print(type(kvpt))



"ОБХОЖДАНЕ НА РЕЧНИК"
# for key in my_dict:
#     print(key)
#
# for values in my_dict.values():
#     print(values)
#
# for key, value in classes.items():
#     print(f"key {key}, value {value}")

# for x in classes.items():
#     print(f"key {x[0]}, value {x[1]}")



"ВРЪЩА ЛИСТ ОТ KEYS или VALUES"
# print(my_dict.items())
# print(classes.keys())
# print(classes.values())

# print(dict.keys(my_dict))
# print(dict.values(my_dict))



"ИЗВИКВАНЕ VALUE ПО КЛЮЧ с GET"     # НЕ гарми ако ключа го няма
# print(my_dict)
# print(my_dict.get(2))
# print(my_dict.get(3))
# print(my_dict.get(3, "Този ключ не съществува"))





"ВРЪЩА СПИСЪК СУМАТА НА VALUE"
# print(sum(num_dict.values()))



"СОРТИРАНЕ"
# print(num_dict)
# print(sorted(num_dict))     # връща лист със сортирани ключове
# print(num_dict)



"СОРТИРАНЕ С ЛАМБДА"
# a, b, c = 10, 20, 5
# dict = {"*": lambda a, b, c: a + b - c}
# print(dict["*"](a, b, c))   # 25
#
# # {'A': 4, 'C': 3, 'B': 1, 'D': 2}
# # връща лист с (key, value) като tuples
# # за sorte с key, lambda прави for-цикъл за всяко „x“ от x[0]
# print(sorted(letter_dict.items(), key=lambda x: x[0]))
# # [('A', 4), ('B', 1), ('C', 3), ('D', 2)]
#
# # {'A': 4, 'C': 3, 'B': 1, 'D': 2}
# # подрежда  (key, value) по value
# print(sorted(letter_dict.items(), key=lambda x: x[0], reverse=True))
# # [('D', 2), ('C', 3), ('B', 1), ('A', 4)]
#
# # подрежда по key и обръща реда
# # {'a': 1, 'b': 2, 'c': 3}
# print(sorted(num_dict.items(), key=lambda x: - x[1]))
# # [('c', 3), ('b', 2), ('a', 1)]
#
# # {'Ines': 27, 'Georgi': 43, 'Pesho': 40, 'Marieta': 37, 'Maria': 52}
# # сортира първо по key и по value
# print(sorted(names_ages.items(), key=lambda x: (x[0], x[1])))
# # [('Georgi', 43), ('Ines', 27), ('Maria', 52), ('Marieta', 37), ('Pesho', 40)]
#
# students_2 = {"A": [5, ], "C": [2, 4], "B": [4, 3, 5]}
# print(sorted(students_2.items(), key=lambda kvpt: len(kvpt[1])))
# # [('A', [5]), ('C', [2, 4]), ('B', [4, 3, 5])]


"OT LIST В РЕЧНИК"
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# print(dict(zip(values, keys)))

# my_dict = {}
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


"ОТ ЕДИН СПИСЪК С DEFAULT"
# keys = ['key1', 'key2', 'key3']
# default_value = 'def_val'
# from_dict = dict.fromkeys(keys, default_value)



"ОТ ЕДИН ЛИСТ С К, V"
# data = [1, 'a', 2, 'b', 3, 'c']
# dict_comp = {data[i]: data[i + 1] for i in range(0, len(data), 2)}



"ДАВА БРОЙКАТА НА KEY"
# print(len(my_dict))



"ИЗПРАЗВАНЕ НА РЕЧНИКА"
# print(my_dict.clear())


"КОПИРА РЕЧНИКА"
# b = my_dict.copy()


"ВРЪЩА СПИСЪК С ТЮПЪЛИ"
# print(num_dict.items())


"ЗАМЕНЯ ЕЛЕМЕНТИ "
# def concatenate(*args, **kwargs):
#     main_string = ''.join(args)
#
#     for key, value in kwargs.items():
#         if key in main_string:
#             main_string = main_string.replace(key, value)
#     return main_string
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))



"ПРОВЕРЯВА ДАЛИ ТЪРСЕНИТЕ ЕЛЕМЕНТИ ГИ ИМА В КЛЮЧОВЕТЕ"
# gifts = {"Gems": 1, "Porcelain": 1, "Gold": 1, "Diamond": 1}
# print({"Gems", "Porcelain"}.issubset(set(gifts.keys())))
# # True


"ЗАМЕНЯ IF statemant"
# storage = {
#     "onion": [5, 1.20],
#     "patato": [10, 0.95],
#     "tomato": [8, 2.40],
#     "pepper": [6, 1.45]
# }
# you_want = input()
# for product in storage.keys():
#     if you_want == product:
#         print(f"We have {product}, {storage[product][0]} kg, {storage[product][1]} lv.")


"ВРЪЩА КЛЮЧ ПО ОПРЕДЕЛЕН ДИАПАЗОН"
# score = int(input(f"give me the score between 100 and 499: "))
# gift_list = {
#     "Gemstone": lambda x: x if 100 <= x <= 199 else None,
#     "Porcelain Sculpture": lambda x: x if 200 <= x <= 299 else None,
#     "Gold": lambda x: x if 300 <= x <= 399 else None,
#     "Diamond Jewellery": lambda x: x if 400 <= x <= 499 else None
# }
# crafted_gifts = {}
#
# # обхождаме всяка възможност в списъка
# for key in gift_list:
#     if gift_list[key](score) is not None:
#         if key not in crafted_gifts:
#             crafted_gifts[key] = 0
#         crafted_gifts[key] += 1
# print(crafted_gifts)



"ДАВА НАЙ-ГОЛЯМАТА СТОЙНОСТ"
# print(max(num_dict_2.keys()))
# print(max(num_dict_2.values()))


"ОБЕДИНЯВА ДВА РЕЧНИКА"
# num_dict_2.update(num_dict)
# print(num_dict_2)


""
# a = {(1, 2): (1, 2), (1, 3): "ard"}
# for key, value in a.items():
#     print(f"{key}: {value}")


""" COMPREHENSION"""
""" COMPREHENSION"""
""" COMPREHENSION"""

# print({value: key for key, value in names_ages.items() if value % 2 == 0})
# # {40: 'Pesho', 52: 'Maria'}

# от тюпъли в дикт
# data = [("Peter", 22), ("Amy", 18), ("George", 35)]
# print({key: value for (key, value) in data})
# print(dict(data))

# num_list = [1, 2, 3, 4]
# print({num: num ** 3 for num in num_list})    # от лист връща dict със стойноста на 3та степен
#
#
# even_years = {}
# for key, value in names_ages.items():
#     if value % 2 == 0:
#         even_years[key] = value
# print(even_years)



"ИЗОМОРФНИ СТРИНГОВЕ"       # пример: egg add
                            # 'e' в Str1 съответства на 'a' в Str2
                            # 'g' в Str1 съответства на 'd' в Str2
def are_isomorphic(str_1: str, str_2: str) -> bool:
    if len(str_1) != len(str_2):
        return False

    dictionary = {}
    for i in range(len(str_1)):
        el_1, el_2 = str_1[i], str_2[i]

        # Проверява дали ключа вече го има
        if el_1 in dictionary.keys():

            # ако го има, проверява дали е равен на вече зададената стойност
            if dictionary[el_1] != el_2:
                # ако не отговаря, значи преди сме въвели друга комбинация
                return False
        else:
            # Проверяваме дали текущия символ от str_2 не е вече закачен към друг ключ
            if el_2 in dictionary.values():
                return False

            # ако и тук го няма, го създаваме
            dictionary[el_1] = el_2
    return True

s1, s2 = 'theeyes', 'theysee'
# s1, s2 = 'theeyes', '1233435'
# s1, s2 = 'theeyes', '1234533'
print(are_isomorphic(s1, s2))




