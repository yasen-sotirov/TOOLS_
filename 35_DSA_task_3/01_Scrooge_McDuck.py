"""
Scrooge McDuck


Scrooge McDuck likes his treasure very much. That is why he likes to
play a funny game. He builds a labyrinth of coins and tries to escape
from it. You can think of the labyrinth as a rectangular field.
Each cell of the field contains 0 or more coins.

When Scrooge McDuck steps on a cell, he can take only a single coin
from this cell, and only if there are any coins. Scrooge McDuck
can escape the field, only if he is surrounded by empty cells.

Scrooge McDuck always wants to go to the neighbouring cell with most
coins. BUT if there are more than one cells with the same amount of
coins (the largest), he chooses a cell (always the largest)
from the order left, right, up, down

If Scrooge McDuck cannot go in any direction, he is out of the labyrinth
Examples

Scrooge McDuck is worried, not about his life, but if the coins he
collect will be enough. Your task is to tell him how many coins he
will collect, following the rules above.

Input
    Read from the standard input
    On the first line find N and M
        The size of the labyrinth
    On the next N lines find M integer values, separated by a space
    The input data will always be valid and there is no need to check
    it explicitly
    The starting location of Scrooge McDuck will be marked as the only 0

Output
    Print to the standard output
    On the single line, print the number of coins Scrooge McDuck can collect, following the rules

Contraints
    2 <= N <= 10
    2 <= M <= 10
    Each cell can contain up to 1024 coins


    Input
4 3
3 2 4
2 0 3
1 1 5
2 2 5

    Output
22

    Input
3 3
10 10 0
10 10 10
10 10 10

    Output
78

    Input
3 3
10 10 10
10 0 10
10 10 10

    Output
80

    Input
2 3
0 5 2
2 5 3

    Output
15


4 3
3 2 4
2 0 3
1 1 5
2 2 5

22


3 3
1 1 1
1 0 1
1 1 1

8
"""

def inside(row_pos, col_pos):
    if 0 <= row_pos < rows and 0 <= col_pos < cols:
        return True
    return False


def next_options(row_pos, col_pos):
    biggest_coin = 0
    row_next, col_next = 0, 0
    rows_opt = [-1, 0, 1, 0]
    cols_opt = [0, 1, 0, -1]

    for ind in range(len(rows_opt)):
        pot_row = row_pos + rows_opt[ind]
        pot_col = col_pos + cols_opt[ind]
        if inside(pot_row, pot_col):
            if matrix[pot_row][pot_col] > biggest_coin:
                biggest_coin = matrix[pot_row][pot_col]
                row_next, col_next = pot_row, pot_col

    if inside(row_pos, col_pos - 1):
        left_coin = matrix[row_pos][col_pos - 1]
    else:
        left_coin = 0

    if inside(row_pos, col_pos + 1):
        right_coin = matrix[row_pos][col_pos + 1]
    else:
        right_coin = 0

    if inside(row_pos - 1, col_pos):
        up_coin = matrix[row_pos - 1][col_pos]
    else:
        up_coin = 0

    if inside(row_pos + 1, col_pos):
        down_coin = matrix[row_pos + 1][col_pos]
    else:
        down_coin = 0

    if biggest_coin == 0:
        return - 1, - 1
    elif left_coin == biggest_coin:
        return row_pos, col_pos - 1
    elif right_coin == biggest_coin:
        return row_pos, col_pos + 1
    elif up_coin == biggest_coin:
        return row_pos - 1, col_pos

    return row_next, col_next



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








