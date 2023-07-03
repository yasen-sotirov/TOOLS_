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
