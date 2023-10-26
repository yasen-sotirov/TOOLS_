"ЛАМБДА"   # ненаименована функция, която се ползва веднъж




"ФИЛТРИРАНЕ НА LIST"
number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
print(list(filter(lambda x: x % 2 == 0, number_list)))
# [4, 8, 6, 2]

# ['cat', 'dog', 'mouse', 'hello', 'world']
print(list(filter(lambda x: len(x) >= 4, letters_list)))
# ['mouse', 'hello', 'world']




# print(list(map(lambda num: num ** 2, number_list)))
#
# print(list(map(lambda x, y: x*y, number_list_2, number_list_3)))



measurement = [
    {'length': 2.5, 'width': 2},
    {'length': 3, 'width': 6},
    {'length': 5, 'width': 4},
]
print(list(map(lambda x: x.get('length', 0) * x.get('width', 0), measurement)))





"LAMBDA"        # анонимна функция (не я декларираме с def) - ползва се само на едно място в кода
                # синтаксис:    lambda променлива: израз

# lam_func = lambda a, b : a * b
# print(lam_func(5, 6))

# name_year = {"ABCC": 4, "CABB": 7, "ABB": 3, "BB": 5, "AB": 2, "AABBB": 1, "BBC": 6}
#
# askii = sorted(name_year, key=lambda x: x)
# print(f"нараства азбучно {askii}")
# print(f"ascending ???   {sorted(name_year, key=lambda x: x[0])}")
# print(f"ascending ???   {sorted(name_year, key=lambda x: x[1])}")
# print(f"нараства азбучно и по дължина {sorted(name_year, key=lambda x: len(x))}")
#
# num_list = []
# for el in askii:
#     char_sum = 0
#     for char in el:
#         char_sum += ord(char)
#     num_list.append(char_sum)
#
# print(num_list)

# print(f"ascending by name length {sorted(name_year, key=lambda x: len(x))}")

# if sort and (sort == 'asc' or sort == 'desc'):
#     result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')