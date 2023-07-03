def sum_row(matrix, r, c):
    if r > 0:
        range_ = range(0, abs(c))  # zero to column
    else:
        range_ = range(abs(c) - 1, len(matrix[0]))  # column to end
    total = 0
    for c in range_:
        total += matrix[abs(r) - 1][c]

    return total


def sum_column(matrix, r, c):
    if c > 0:
        range_ = range(0, abs(r))  # zero to row
    else:
        range_ = range(abs(r) - 1, len(matrix))  # row to end

    total = 0

    for r in range_:
        total += matrix[r][abs(c) - 1]

    return total


matrix = []

for x in range(int(input())):
    matrix.append(list(map(int, input().split())))

best_sum = -100000

coords = list(map(int, input().split()))

for i in range(0, len(coords), 2):
    row, col = coords[i], coords[i + 1]

    current_sum = (

            sum_row(matrix, row, col)

            + sum_column(matrix, row, col)

            - matrix[abs(row) - 1][abs(col) - 1]  # remove intersection

    )

    best_sum = max(current_sum, best_sum)

print(best_sum)