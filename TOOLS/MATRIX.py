"MATRIX"    # най-важна библиотека за матрици NumPy


list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


"СЪЗДАВАНЕ НА МАТРИЦА"
# rows = 3
# cols = 5
# for r in range(rows):
#     for element_in_current_row in range(cols):
#         print("*", end=" ")
#     print()


"ПЪЛНЕНЕ НА МАТРИЦАТА"
# 3
# 2 4 6
# 8 10 12
# 14 16 18

# matrix = []
# row_number = int(input())
# for _ in range(row_number):
#     next_row = input().split()
#     matrix.append(next_row)
# print(matrix)


"ДОСТЪПВАНЕ В ЛИСТА"
# print(list_2d[1][1])      # достъпване на елементи


"ОБХОЖДА ЛИСТА"
for row in list_2d:     # обхожда по елементи
    for el in row:
        print(el, end=" ")
#     print()

# for row in range(len(list_2d)):         # обхожда по индекси
#     for col in range(len(list_2d)):
#         el = list_2d[row][col]
#         print(f'[{row}][{col}] = {el}')



"ПРОМЯНА В ЛИСТА"
# list_2d[1] = [1, 2, 3]      # промяна на цял ред
# print(list_2d)

# list_2d[1][1] = 11      # промяна на елемент
# print(list_2d)


"СЪЗДАВАНЕ НА ПРАЗНА МАТРИЦА С РАЗМЕР n"
# n = int(input('type num for matrix size: '))
# matrix = [[0] * n for _ in range(n)]
# print(matrix)

# matrix = []
# for _ in range(n):
#     matrix.append([0] * n)
# print(matrix)


"ПРИНТИРАНЕ НА МАТРИЦА"
# for row in list_2d:
#     print(" ".join(str(el) for el in row))


# lst = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# for x, y, z in lst:
#     print(f"x {x} : y {y} : z {z}")


# counter = 0
# for row in range(3):
#     for col in range(3):
#         print(counter, end=" ")
#         counter += 1
#     counter -= 2
#     print()
#
# 0 1 2
# 1 2 3
# 2 3 4




"ОБХОЖДАНЕ НАД ДИАГОНАЛА"
# total_sum = 0
# for row in range(len(list_2d)):
#     for col in range(len(list_2d)):
#         if col > row:
#             total_sum += list_2d[row][col]
# print(total_sum)
