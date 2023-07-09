"DICTIONARIES"      # values - mutable - променлив. може да се добавя променя ...
                    # keys - immutable - ключовете са уникални
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
# my_dict["eyes color"] = "green"
# print(my_dict)
#
# # при валю списък
# # дава ни достъп до вложения лист
# names = classes["1A"]
# # както обикновен лист
# names.append("appended name")
#
# for key in classes:
#     classes[key].append("from the loop")
# print(classes)



"ПРОМЯНА В РЕЧНИКА"
# my_dict["eyes color"] = "green"
# my_dict["b"] = 30
#
# # дава ни достъп до листа и работим с него
# names = classes["1A"]
# # както обикновен лист
# names.append("appended name")
# print(classes)
#
# for key in classes:
#     classes[key].append("from the loop")
# print(classes)


"ОБХОЖДАНЕ НА РЕЧНИК"
# for key in my_dict:
#     print(key)
#
# for _ in my_dict.values():
#     print(_)
#
# for key, value in classes.items():
#     print(f"key {key}, value {value}")
#
# for x in classes.items():
#     print(f"key {x[0]}, value {x[1]}")
#     # key 1A, value ['Ines', 'Pesho']
#     # key 1B, value ['Ivan', 'Maria']


"ВРЪЩА ЛИСТ С KEY, VALUE"
# print(my_dict.items())
# dict_items([('a', 25), ('b', 'Pesho'), (2, 33)])


"ВРЪЩА ЛИСТ С KEY"
# # {'1A': ['Ines', 'Pesho'], '1B': ['Ivan', 'Maria']}
# print(classes.keys())
# # dict_keys(['1A', '1B'])  <class 'dict_keys'>


"ВРЪЩА ЛИСТ С VALUE"
# # {'1A': ['Ines', 'Pesho'], '1B': ['Ivan', 'Maria']}
# print(classes.values())
# # dict_values([['Ines', 'Pesho'], ['Ivan', 'Maria']])
# # <class 'dict_values'>


"ИЗВИКВАНЕ VALUE ПО ИНДЕКС"
# {'1A': ['Ines', 'Pesho'], '1B': ['Ivan', 'Maria']}
names = classes['1A']
print(names[0])         # Ines
print(names[0][0:2])    # In


"ИЗВИКВАНЕ VALUE ПО КЛЮЧ"
# # гарми ако ключа го няма!
# print(my_dict["b"])
#
# # НЕ гарми ако ключа го няма
# print(my_dict.get(2))
# print(my_dict.get(3))

"ИЗВИКВАНЕ VALUE OT ВЛОЖЕН РЕЧНИК"
# # {'1A': ["Ines", "Pesho"],
# # '1B': ["Ivan", "Maria"]}
# print(classes['1A'][1])
# # Pesho
#
# print(students['№1']['name'])
# # Pesho


"ВРЪЩА СПИСЪК СУМАТА НА VALUE"
# print(sum(num_dict.values()))


"ПРЕМАХВА K-V ДВОЙКА"
# # {'a': 25, 'b': 'Pesho', 2: 33}
# # трие по ключ
# # {'a': 25, 'b': 'Pesho', 2: 33}
# del my_dict['a']
# # {'b': 'Pesho', 2: 33}
#
# # трие по ключ и пази
# key = my_dict.pop("b")
# # {'a': 25, 2: 33}
# # Pesho
#
# # трие последната двойка и пази
# # {'a': 25, 'b': 'Pesho', 2: 33}
# a = my_dict.popitem()
# print(my_dict)      # {'a': 25, 'b': 'Pesho'}
# print(a)            # (2, 33)
#
# # трие цялата променлива
# dictionary = my_dict
# del dictionary


"СОРТИРАНЕ"
# # {'a': 1, 'b': 2, 'c': 3}
# # връща лист със сортирани ключове
# print(sorted(num_dict))
# # ['a', 'b', 'c']



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


"OT СПИСЪЦИ В РЕЧНИК"     #
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# print(dict(zip(values, keys)))
#
# my_dict = {}
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


"ДАВА БРОЙКАТА НА KEY"
# print(len(my_dict))


"ТЪРСЕНЕ В РЕЧНИК"
# # търси в ключа
# print("a" in num_dict)  # True
# print("f" in num_dict)  # False
#
# # търси в value
# print(3 in num_dict.values())  # True


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



"DEMO"
# # define a dict = { 'key': 'value' }
# phonebook = {
#     'Alice': '081231938',
#     'Bob': '078712312',
#     'Charlie': '081200912'
# }
#
# # access value by key
# print(phonebook['Alice'])
# print(phonebook.get('Alice'))
#
# # Throws error if key does not exist
# # print(phonebook['alice'])
#
# # check if key exists
# print('Alice' in phonebook)
#
# # change existing value
# phonebook['Alice'] = '033333123'
#
# # add new value
# phonebook['Donn'] = '089787123'
#
# # get number of key:value pairs
# print(len(phonebook))
#
# # get a collection of all keys in the dict
# keys = phonebook.keys()  # also has .values()
# for key in keys:
#     print(key)
#
#
#
# # deletes a key:value pair
# phonebook.pop('Alice') # will return 081231938
# # del phonebook['Alice'] # returns nothing
#
# print(len(keys))  # the keys collection is also implicitly updated
