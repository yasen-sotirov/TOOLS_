"ТЪРСЕЩИ  АЛГОРИТМИ"   #
# алгоритми проверяващи дали определена стойност се съдържа структура от данни
# Sequential - линейни: for el in num_list:
# Interval - интервани: работят с подредени масиви

nums = [6, 8, 9, 11, 14, 17, 22, 23, 25, 28, 30]

"HASH TABLES"   # търсене с константна сложност


"БИНАРНО ТЪРСЕНЕ"   # работи с сортирани списъци, логаритмична сложност
# def binary_search_iter(target, num_list: list[int]):
#     start = 0
#     end = len(num_list) - 1
#     while start <= end:
#         mid_ind = (start + end) // 2
#         if num_list[mid_ind] > target:
#             end = mid_ind - 1
#         elif num_list[mid_ind] < target:
#             start = mid_ind + 1
#         else:
#             return mid_ind
#     return "Number not found"
# print(binary_search_iter(6, nums))


"БИНАРНО ТЪРСЕНЕ recursive"
# def binary_search_rec(target, num_list, start, end):
#     if start > end:
#         return "Number not found"
#
#     mid_ind = (start + end) // 2
#     if num_list[mid_ind] < target:
#         return binary_search_rec(target, num_list, mid_ind + 1, end)
#     elif num_list[mid_ind] > target:
#         return binary_search_rec(target, num_list, start, mid_ind - 1)
#     else:
#         return mid_ind
# print(binary_search_rec(6, nums, 0, len(nums) - 1))







"===== СОРТИРАЩИ АЛГОРИТМИ ====="
# подреждат елементите в една колекция
# Timsort - посредством вградения в Питон sorted()


"СОРТИРАНЕ НА ОБЕКТИ с LAMBDA"   # при типове, които ние сме дефинирали:
# int и str знаят вътрешно как да се сравняват помежду си

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'({self.name}, {self.age})'


people = [Person('Petar', 35), Person('Ivan', 20), Person('Dimitar', 30)]
ordered_people = sorted(people, key=lambda p: p.name)

# print(ordered_people)
# print(*ordered_people, sep='\n')




"СОРТИРАНЕ НА ОБЕКТИ с LOWER THAN"   # при типове, които ние сме дефинирали:
# int и str знаят вътрешно как да се сравняват помежду си

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'({self.name}, {self.age})'
#
#     "LOWER THAN" # magic метод сравняващ обект с друг обект
#     def __lt__(self, other):
#         return self.name < other.name
#         # сравнява дали името е по-малко по азбучен ред
#         # от името на друг обект от същия клас
#
#
# people = [Person('Petar', 35), Person('Ivan', 20), Person('Dimitar', 30)]
# ordered_people = sorted(people)
#
# print(ordered_people)
# print(*ordered_people)



