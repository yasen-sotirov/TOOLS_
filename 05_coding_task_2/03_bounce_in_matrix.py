def is_border(position, row_p, col_p):
    flag = False
    if row_p == 0 or row_p == rows - 1:
        flag = True
    if col_p == 0 or col_p == cols - 1:
        flag = True
    return flag


def direction():
    pass


rows, cols = [int(x) for x in input().split()]
matrix = []
row_start = 1

for r in range(rows):
    row_input = []
    col_start = row_start
    for c in range(cols):
        row_input.append(col_start)
        col_start = col_start * 2
    row_start = row_start * 2
    matrix.append(row_input)

path = []
row_position = 0
col_position = 0

while True:

    direction = [1, 1]
    next_position = [0, 0]
    next_position[0] = row_position + direction[0]
    next_position[1] = col_position + direction[1]
    value_on_position = matrix[next_position[0]][next_position[1]]
    path.append(value_on_position)
    break
















