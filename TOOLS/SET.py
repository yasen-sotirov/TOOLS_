"SET {} "   # само уникални елементи
# Mutable - може да бъде променян след като бъде създаден
# Abstract Data Structure
# не подрежда елементите!

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
set_3 = {3, 4}
set_4 = {'Argentina', 'Bulgaria', 'Congo'}
set_5 = {"1", "2", "3", "4"}



"СЪЗДАВАНЕ SET"
# a = set()          # иначе се бърка с речник
# a = {}             # питона го мисли за дикшанъри


"ИТЕРИРА ХАОТИЧНО СТРИНГОВЕТЕ"
# for el in set_1:
#     print(el, end=" ")
# print()
#
# for el in set_4:
#     print(el, end=" ")
# print()
#
# for el in set_5:
#     print(el, end=" ")


# "ДОБАВЯ ЕЛЕМЕНТИ"
# print(set_1)
# set_1.add(12)
# print(set_1)


"ДЪЛЖИНАТА НА СЕТА"
# print(len(set_1))


"ТРИЕ ЕЛЕМЕНТ НА ИНДЕКС - гърми ако ел го няма"
# print(set_1)
# set_1.remove(3)
# print(set_1)


"ТРИЕ КОНКРЕТЕН ЕЛЕМЕНТ"
# set_4.remove("Congo")
# print(set_4)


"ТЪРСИ КОНКРЕТЕН ЕЛЕМЕНТ"
# print("Congo" in set_4)     # True
# print(2 in set_4)           # False


"ТРИЕ КОНКРЕТЕН ЕЛЕМЕНТИ - НЕ гърми ако ел го няма"
# print(set_1)
# set_1.discard(3)
# print(set_1)

# print(set_2)
# set_2.discard(1000)
# print(set_2)


"ТРИЕ ПЪРВИЯ ЕЛЕМЕНТ И ГО ПАЗИ"
# # {1, 2, 3, 4}
# set_1.pop()
# # {2, 3, 4}
# print(set_1.pop())
# # 2


"ДАВА ЕЛЕМЕНТИТЕ, КОИТО ГИ НЯМА ВЪВ ВТОРИЯ СЕТ"     # Difference
# print(set_1)
# print(set_2)
# print(set_1 - set_2)
# print(set_2 - set_1)


"ДАВА ЕДНАКВИТЕ ЕЛЕМЕНТИ В ДВА СЕТА"        # Intersection
# print(set_1)
# print(set_2)
# print(set_1 & set_2)
# print(set_1.intersection(set_2))
# връща ново множество


"ДАВА ЕЛЕМЕНТИ, КОИТО СА УНИКАЛНИ ЗА ДВАТА СЕТА"     # Symmetric Difference
# print(set_1)
# print(set_2)
# print(set_1 ^ set_2)
# print(set_1.symmetric_difference(set_2))


"ОБЕДИНЯВА ДВА СЕТА"
# print(set_1)
# print(set_2)
# print(set_1 | set_2)
# print(set_1.union(set_2))


"ВСИЧКИ ЕЛЕМЕНТИ НА ЕДИНИЯ ИМА ЛИ ГИ В ДРУГИЯ"   # Subset
# print(set_2)
# print(set_3)
# print(set_2 > set_3)        # всички елементи на set_3 има ли ги в set_2
# print(set_3 > set_2)        # всички елементи на set_2 има ли ги в set_3
# print()
# print(set_1.issubset(set_2))        # set_1 <= set_2
# print(set_1.issuperset(set_2))      # set_1 >= set_2


"SET COMPREHENSION"
# nums = [1, 2, 3, 4, 5, 5, 6, 6, 2, 1]
# set_comprehension = {el for el in nums}
# print(set_comprehension)
# print(set(nums))            # или на кратко


"СОРТИРАНЕ - превръща в лист и сортира"
# print(set_1)
# set_1.add(-2)
# set_1.add(-12)
# set_1.add(-1)
# print(set_1)
# print(sorted(set_1))


"ГЕНЕРИРА SET C RANGE ОТ ЧИСЛА"
# print(set(range(1, 12, 2)))


"НЕПРОМЕНЛИВ СЕТ"       # сет, който не можем да променяме
# a = frozenset([1, 2, 3, 3])
# print(a)
# print(type(a))
#
# a = {1, 2, 3}       # или сета го правим на тюпъл
# b = tuple(a)


"ПРЕМАХВА ПОВТАРЯЩИТЕ СЕ ЕЛЕМЕНТИ ОТ ЛИСТА - SET"   # разбърква елементите
# print(list(set(mix_list)))


