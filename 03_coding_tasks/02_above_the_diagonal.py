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

matrix_size = int(input())
matrix = []
counter = 1

for row in range(matrix_size):
    sub_matrix = []
    for col in range(matrix_size):
        row_el = counter * 2
        sub_matrix.append(row_el)
    counter *= 2
    print()

print(matrix)

