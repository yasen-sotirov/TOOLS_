"""
4 3
3 2 4
2 0 3
1 1 5
2 2 5

22
"""

def inside(row_pos, col_pos):
    if 0 <= row_pos < rows and 0 <= col_pos < cols:
        return True
    return False


def next_options(row_pos, col_pos):
    max_coin = 0
    row_max = 0
    col_max = 0
    options = []
    options_coord = []
    #            3  2  4  1
    #            u  r  d  l
    rows_opt = [-1, 0, 1, 0]
    cols_opt = [0, 1, 0, -1]

    for ind in range(len(rows_opt)):
        potential_row = row_pos + rows_opt[ind]
        potential_col = col_pos + cols_opt[ind]
        if inside(potential_row, potential_col):
            options[ind] = matrix[potential_row][potential_col]
            options_coord[ind] = (potential_row, potential_col)

        if options[3] == options[0] or options[3] == options[1] or options[3] == options[2]:
            return options[3]

        elif options[1] == options[0] or options[1] == options[2]:
            return options[1]

        elif options[0] == options[2]:
            return options[0]

        elif potential_position > max_coin:
            max_coin = potential_position
            row_max = potential_row
            col_max = potential_col
    if max_coin > 0:
        return row_max, col_max
    return -1, -1



rows, cols = map(int, input().split())
matrix = []
start_row = 0
start_col = 0
counter = 0

for row in range(rows):
    col = [int(el) for el in input().split()]
    if 0 in col:
        start_row = row
        start_col = col.index(0)
    matrix.append(col)


while True:
    current_row, current_col = next_options(start_row, start_col)
    if current_row == -1 and current_col == -1:
        break
    counter += 1
    matrix[current_row][current_col] -= 1
    start_row, start_col = current_row, current_col

print(counter)








