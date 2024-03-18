"TUPLES () "    # IMmutable - НЕпроменлив
                # пази реда на елементите

t_1 = (5, 0, "Gosho", 2, 4)
t_2 = (1,)                  # без "," питона го мисли за уравнение
t_3 = (1, 2, 3, 4, 5, 6, 7)
t_4 = (("a", 5), ("b", 3), ("c", 1))



"ПОКАЗВА КАКВО ИМА НА ИНДЕКС"
# print(t_1[1])


"ПОКАЗВА НА КОЙ ИНДЕКС СЕ НАМИРА ЕЛЕМЕНТ"
# print(t_1.index("Gosho"))


"ПОКАЗВА ОТ ИНДЕКС ДО ИНДЕКС"
# print(t_3)
# print(t_3[1:4])
# print(t_3[::2])
# print(t_3[:3])
# print(t_3[-4:-1])


"ИТЕРИРАНЕ"
# for x in t_1:
#     print(x)


"ТЪРСИ В ТЮПЪЛА"
# print("pesho" in t_1)   # False
# print("Gosho" in t_1)   # True


"ДЪЛЖИНА НА ТЮПЪЛА"
# print(t_3)
# print(len(t_3))


"MIN MAX"
# print(min(t_3))
# print(max(t_3))



"БРОЙ ЕЛЕМЕНТИТЕ"
# print(t_1.count(t_1))


"ОТВАРЯ ТЮПЪЛА"
# a, b, *c = t_1
# print(a)
# print(b)
# print(c)

# a= (1,)
# print(a[0])


"ОБЕДИНЯВАНЕ НА ДВА ТЮПЪЛА"
# print(t_1 + t_3)


"УМНОЖАВАНЕ НА ЕЛЕМЕНТИТЕ"
# print(t_2)
# print(t_2 * 8)


"ГЕНЕРИРА TUPLE C RANGE ОТ ЧИСЛА"
# print(tuple(range(1, 10 + 1)))


"СОРТИРАНЕ"
# sorted_result = sorted(t_4, key=lambda kvpt: kvpt[1])
# for key, value in sorted_result:
#     print(f"{key} - {value}")


"ДОБАВЯНЕ КЪМ TUPLE"
# tup = (1, 2, 3)
# tup += (3, 4, 5)
# print(tup)
# print(type(tup))


"ДАЛИ Е SUBTUPLE OT ДРУГ TUPLE"
# def contains_subtuple(sub_tuple, the_tuple):
#     if len(sub_tuple) > len(the_tuple):
#         return False
#     else:
#         for index in range(len(the_tuple) - len(sub_tuple) + 1):
#             if the_tuple[index:index + len(sub_tuple)] == sub_tuple:
#                 return True
#     return False
#
# print(contains_subtuple((2, 3), (1, 2, 3)))     # True
# print(contains_subtuple((1, 3), (1, 2, 3)))     # False
