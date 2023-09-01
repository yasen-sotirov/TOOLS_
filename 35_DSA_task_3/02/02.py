#
# def inside(row_pos, col_pos):
#     if 0 <= row_pos < rows and 0 <= col_pos < cols:
#         return True
#     return False
#
#

#
#
# rows, cols = map(int, input().split())
# matrix = []
# counter = 0
#
# for row in range(rows):
#     col = [int(el) for el in input().split()]
#     matrix.append(col)
#







def in_bounds(r, c, lab):
    if r < 0 or r >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    return True


def find_path(row, col, matrix, step):
    print(row, col)

    matrix[row][col] = 0

    if in_bounds(row + 1, col, matrix) and matrix[row + 1][col] == 1:
        find_path(row + 1, col, matrix, step + 1)

    if in_bounds(row, col + 1, matrix) and matrix[row][col + 1] == 1:
        find_path(row, col + 1, matrix, step + 1)

    if in_bounds(row, col - 1, matrix) and matrix[row][col - 1] == 1:
        find_path(row, col - 1, matrix, step + 1)

    if in_bounds(row - 1, col, matrix) and matrix[row - 1][col] == 1:
        find_path(row - 1, col, matrix, step + 1)


rows, cols = map(int, input().split())
matrix = []
counter = 0

for row in range(rows):
    col = [int(el) for el in input().split()]
    matrix.append(col)

find_path(0, 0, matrix, 0)
for el in matrix:
    print(el)


# 4 4
# 1 0 0 1
# 1 0 1 1
# 1 0 1 0
# 1 1 1 0