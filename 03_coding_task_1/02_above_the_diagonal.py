"""
Above the Main Diagonal
You are given a number N. Using it, create a square matrix of numbers,
formed by powers of 2 and find the sum of the numbers above the main diagonal,
excluding the diagonal itself.

Input
Read from the standard input.
    On the first line, read the number N - the number of rows and columns.

Output
Print to the standard output.
    On a single line print the sum of the numbers above the main diagonal
    excluding the diagonal.

Constraints
    N can get as big as 30.

Sample tests
Input
4

Output
70

Explanation
With N equal to 4, we will have a matrix that looks like this:

1 2 4 8
2 4 8 16
4 8 16 32
8 16 32 64

The main diagonal is 1 4 16 64, so the sum of the numbers above it:
2 + 4 + 8 + 8 + 16 + 32 = 70.
"""

size = int(input())
matrix = []
row_start = 1

# за всеки зададен ред от матрицата правим нов ред
for _ in range(size):
    # този нов ред е празен
    row = []
    # всяка колона започва от зададения роу–стар който се променя
    col = row_start
    # итерирам през всяка колона
    for _ in range(size):
        # и добавям колоната
        row.append(col)
        # редактирам колоната
        col *= 2
    # готовият ред го добавям към матрицата
    matrix.append(row)
    # редактирам старта на реда
    row_start *= 2

# обхождане на матрицата
total_sum = 0
# итерирам през индексите
for row in range(size):
    for col in range(size):
        if col > row:
            total_sum += matrix[row][col]

print(total_sum)
