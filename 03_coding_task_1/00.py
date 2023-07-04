side = int(input())

# create the matrix

matrix = []
row_start = 1

for r in range(side):
    row = []
    col_start = row_start

    for c in range(side):
        row.append(col_start)
        col_start = col_start * 2
    row_start = row_start * 2
    matrix.append(row)

# find the sum

total = 0
for r in range(side):
    for c in range(side):
        if c > r:
            total += matrix[r][c]

print(total)