"LISTS"         # съхранява различни типове данни на едно място
                # референтен тип данни:  names = [1, 2, 3]  asd = names - едно и също са
                # лист с методите  https://www.w3schools.com/python/python_ref_list.asp
                # mutable - променлив

mix_list = [1, 3, 2, "a", "b", 4, 88, 2, 2]
number_list = [1, 4, 3, 8, 6.59, 2.32]
number_list_2 = [10, 20, 30, 40, 50, 60]
number_list_3 = [1, 2, 3, 4, 5]
letters_list = ["cat", "dog", "mouse", 'world']
nested_list = [[1, 2, 3], [4, 5, 6]]

"ДОБАВЯ НОВИ ЕЛЕМЕНТИ В ЛИСТА"
# print(mix_list)
# mix_list.append("new_var")
# mix_list.append(-int(2) * 2)
# print(mix_list)

# [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# [1, 3, 2, 'a', 'b', 4, 88, 2, 2, 'new_var', -4]


"LIST ФУНКЦИЯ"
a = "012abv"
print(list(a))
# ['0', '1', '2', 'a', 'b', 'v']

"ДОБАВЯ ЕЛЕМЕНТИ КЪМ ЛИСТА"
# lst = [1, 2, 3]
# for _ in range(3):
#     lst += [0]
#     print(lst)
#
# # [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
# number_list[0] += 100
# # [101, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
#
# # ['cat', 'dog', 'mouse', 'hello', 'world']
# letters_list[0] += '_MO'
# # ['cat_MO', 'dog', 'mouse', 'hello', 'world']


"ЗАМЕНЯ СЪЩ ЕЛЕМЕНТИ В ЛИСТА"
# # ['cat', 'dog', 'mouse', 'hello', 'world']
# letters_list[0] = "TOM"
# # ['TOM', 'dog', 'mouse', 'hello', 'world']


"ОБЕДИНЯВА ДВА ЛИСТА"       # или само един string
# list_1 = [1, 2, 3]
# list_2 = ['cat', 'dog', 'mouse']
# list_1.extend(list_2)
# print(list_1)
# # [1, 2, 3, 'cat', 'dog', 'mouse']
#
# print(list_2 + list_2)
# # ['cat', 'dog', 'mouse', 'cat', 'dog', 'mouse']


"ОБЕДИНЯВА ЛИСТА В STRING"       # само за str;  *number_list за int
# print('-'.join(letters_list))
# # cat-dog-mouse-hello-world
#
# print(' '.join(letters_list))
# # със " " все едно конкатенираме текста
#
# print('\n'.join(letters_list))
# # печати всеки елемент на нов ред
#
# # [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
# print(", ".join([str(x) for x in number_list]))
# # ако са числа
# # 1, 4, 3, 8, 6, 2, 7, 6.59, 2.32


"ОБХОЖДА ВЛОЖЕН СПИСЪК"
# lst = [[1, 1], [2, 2], [3, 3]]
# for x, y in lst:
#     print(f"x {x} : y {y}")


"РАЗОПАКОВА ЛИСТА"      # вместо " ".join(), защото той работи само с str
# num_list = [1, 4, 3]
# print(*num_list)
# # 1 4 3
#
# print(*num_list, sep=", ")
# # 1, 4, 3



"НАЙ-МАЛКО И НАЙ-ГОЛЯМО ЧИСЛО"
# print(min(number_list))
# print(max(number_list))


"РАЗМЕСТВАНЕ В ЛИСТА"
# nums = [10, 20]
# nums[0], nums[1] = nums[1], nums[0]
# print(nums)     # [20, 10]



"ТРИЕ / ВАДИ ПО ИНДЕКС (или последния) СИМВОЛ ОТ ЛИСТА"
# [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# char = mix_list.pop(-3)
# print(mix_list) # [1, 3, 2, 'a', 'b', 4, 2, 2]
# print(char)     # 88


"ИЗВЕЖДА ЕЛЕМЕНТ ОТ ЛИСТА"
# броя на променливите трябва да отговаря на дължината на листа
# num_1, num_2, num_3, num_4, num_5 = number_list_3
# print(num_1)
# print(num_5)


"ПРЕМАХВА ЕЛЕМЕНТ/И В ЛИСТА (от ляво на дясно)"
# # ако елемента го няма връща грешка
# # [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# mix_list.remove(2)
# # [1, 3, 'a', 'b', 4, 88, 2, 2]
#
# while "dog" in letters_list:
#     letters_list.remove("dog")
# print(letters_list)


"ТРИЕ ЕЛЕМЕНТ ПО ИНДЕКС"
# # [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# del mix_list[1]
# # [1, 2, 'a', 'b', 4, 88, 2, 2]
#
# del mix_list[1:5]
# # [1, 'a', 'b', 4, 88, 2, 2]



"СУМИРА ЛИСТА"
# print(sum(number_list))
# # 39.910000000000004
#
# print("{:.2f}".format(sum(number_list)))
# # 39.91



"ВМЪКВА (нещо) ПО ИНДЕКС"
# [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# mix_list.insert(3, "Pesho")
# [1, 3, 2, 'Pesho', 'a', 'b', 4, 88, 2, 2]


"ПЪЛНЕНЕ НА ЛИСТ"
# number_of_wagon = 5
# train = [0] * number_of_wagon
# [0, 0, 0, 0, 0]


"НА КОЙ ИНДЕКС СЕ НАМИРА (нещо)"
# [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# number = mix_list.index('b')
# print(number)   # 4


"БРОЙ КОЛКО (спец. неща) ИМА В ЛИСТА"
# не работи със стрингове
# list_nums = [1, 2, 1, 5, 1, 6]
# print(list_nums.count(1))      # 3


"ДАВА ЕЛЕМЕНТА И ИНДЕКСА НА КОЙТО СЕ НАМИРА"
# # [1, 3, 2, 'a', 'b', 4, 88, 2, 2]
# for index, letter in enumerate(mix_list):
#     print(index, letter, sep='-', end=', ')
#     # 0 - 1, 1 - 3, 2 - 2, 3 - a, 4 - b, 5 - 4, 6 - 88, 7 - 2, 8 - 2,



"КОПИРА ЛИСТА"
# и работим върху копието, оригинала се запазва
# second_list = mix_list.copy()
# second_list.append(1000)
# print(mix_list)
# print(f'second list: {second_list}')
# second list: [1, 3, 2, 'a', 'b', 4, 88, 2, 2, 1000]


"ВРЪЩА ЕЛЕМЕНТИ ЗАПОЧВАЩИ С (нещо)"
# words = ['cat', 'dog', 'mouse', 'dolphin']
# print(list([x for x in words if x.startswith("d")]))
# ['dog', 'dolphin']

"ТЪРСЕНЕ В ЛИСТ"
# if 'a' in mix_list:
#     print('ok')


"СОРТИРА СЪЩ. ЛИСТ"
# # ['cat', 'dog', 'mouse', 'hello', 'world']
#
# letters_list.sort()
# print(letters_list)
# # ['cat', 'dog', 'hello', 'mouse', 'world']
#
# letters_list.sort(reverse=True)
# print(letters_list)
# # ['world', 'mouse', 'hello', 'dog', 'cat']


"ПРАВИ НОВ ЛИСТ И СОРТИРА НЕГО"
# name_list = ["Ali", 'Marry', 'Kim', 'Teddy', 'Monika', 'John']
# sorted_list = sorted(name_list, key=lambda item: (-len(item), item))
# print(sorted_list)
# ['Monika', 'Marry', 'Teddy', 'John', 'Ali', 'Kim']


"ОБРЪЩА ЛИСТА ОТЗАНД НАПРЕД"
# mix_list.reverse()
# print(mix_list)


"ПРОМЕНЯ ЕЛЕМЕНТИ ВЪВ ВЛОЖЕНИЯ СПИСЪК"
# [[1, 2, 3], [4, 5, 6]]
# nested_list[0][1] = 222
# [[1, 222, 3], [4, 5, 6]]


"КОПИРАНЕ НА ВЛОЖЕН СПИСЪК"
# from copy import deepcopy
# # [[1, 2, 3], [4, 5, 6]]
# nested_list_2 = deepcopy(nested_list)
# # [[1, 2, 3], [4, 5, 6]]


"ОБХОЖДА ЛИСТА ПО ЕЛЕМЕНТ И ПО ИНДЕКС - итерира"
# # показва индексите на листа
# for index in range(0, len(mix_list)):
#     print(index, end=", ")
#     # 0, 1, 2, 3, 4, 5, 6, 7, 8,
#
# # извиква елемент по индекса му
# for index in range(0, len(mix_list) - 5):
#     print(mix_list[index], end=', ')
#     # 1, 3, 2, a,


"СРЕДНА СТОЙНОСТ НА ЛИСТА"
# from statistics import mean
# print(f"средна стойност: {mean(number_list):.2f}")
# # средна стойност: 4.43


"ФИЛТЪР - елементите, които дават True"
# letters = ['a', 'e', 'i', 'o', 'u']
#
# def only_vowel(variable):
#     return variable in letters
#
# sequence = ['a', 'g', 'e', 'e', 'u', 'k', 'p' 'a']
# print(list(filter(only_vowel, sequence)))
# # ['a', 'e', 'e', 'u']
#
# # [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
# print(list(filter(lambda x: x % 2 == 0, number_list)))
# # [4, 8, 6, 2]
#
# # ['cat', 'dog', 'mouse', 'hello', 'world']
# print(list(filter(lambda x: len(x) >= 4, letters_list)))
# # ['mouse', 'hello', 'world']



"MAP - работи с итерируеми обекти"
# # ['cat', 'dog', 'mouse', 'hello', 'world']
# print(list(map(len, letters_list)))
# # [3, 3, 5, 5, 5]

# # [1, 4, 3, 8, 6.59, 2.32]
# print(number_list)
# def cubed_num(digit):
#     return digit ** 2
# print(list(map(cubed_num, number_list)))
# # [1, 16, 9, 64, 43.4281, 5.3824]

# # ['cat', 'dog', 'mouse', 'world']
# print(list(map(str.upper, letters_list)))
# # ['CAT', 'DOG', 'MOUSE', 'WORLD']

# # [1, 4, 3, 8, 6.59, 2.32]
# print(list(map(float, number_list)))
# # [1.0, 4.0, 3.0, 8.0, 6.59, 2.32]

# x, y = map(int, input().split())
# print(f"{type(x)} {x}, {type(y)} {y}")


"ИЗПРАЗВА ЛИСТА"
# clear_list = mix_list.clear()
# print(clear_list)



"ОБРЪЩА ЛИСТА"
# или слайсинг letters_list[::-1]

# прави нова колекция, която е обърната
# print(list(reversed(letters_list)))

# обръща оригиналната колекция
# print(letters_list.reverse())


"BOOLEAN с IN ОПЕРАТОРА"            # ако го има в листа връща True
# boolean = 5 in number_list_3
# print(boolean)  # True
#
# print(6 in number_list_3)
# # False


"ГЕНЕРИРА ЛИСТ C RANGE ОТ ЧИСЛА"
# print(list(range(1, 8 + 1, 2)))
# [1, 3, 5, 7]


"ЕДНАКВИ ЛИ СА"
# връща дали всичк в итеръбъла са еднакви

# [10, 20, 30, 40, 50, 60]
# print(all([isinstance(x, int) for x in number_list_2]))
# True

# print([isinstance(x, int) for x in number_list_2])
# [True, True, True, True, True, True]


"С КОЛКО ИЗЛИЗАМ ОТ ЛИСТА"
# array = [0, 1, 2, 3, 4, 5]
# position = 4
# size = 3
# new_position = (position + size) % len(array)
# print(new_position)     # 1






"""COMPREHENSIONS"""
"""COMPREHENSIONS"""
"""COMPREHENSIONS"""



"ОБХОЖДА ЛИСТА И ПРЕВРЪЩА ЕЛЕМЕНТИТЕ"
# print(number_list)
# print([str(el) for el in number_list])


"ОБХОЖДА ЛИСТА И СРАВНЯВА ДАЛИ ГИ ИМА В ДРУГИЯ ЛИСТ"
# print([item for item in number_list if item in number_list_2])


"СОРТИРА ЛИСТА"
# data = ["5", "Sofia"]
# digit = [int(x) if x.isdigit() else x for x in data]
# print(digit)

# print([x * 2 for x in number_list if x % 2 == 0])


"ВСИЧКИ ЛИ СА ЕДНАКВИ"              # връща дали всичк в листа са еднакви
# # print(all(number_list_2))
# print(all([isinstance(x, int) for x in number_list_2]))
# print(all([isinstance(x, str) for x in letters_list]))
# print(all([isinstance(x, str) for x in mix_list]))


"САМО ЕДНО ДА Е ВЯРНО"
# print(any([True, False, False]))


"ВРЪЩА ЕЛЕМЕНТИ ЗАПОЧВАЩИ С (нещо)"
# letters = ['cat', 'dog', 'mouse', 'dolphin']
# print(list([item for item in letters if item.startswith("d")]))
# # ['dog', 'dolphin']
