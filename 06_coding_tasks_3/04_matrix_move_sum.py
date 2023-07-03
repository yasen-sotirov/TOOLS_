"""
Matrix Max Sum

Write a program that finds the maximum sum between two given coordinates in a matrix.
The coordinates are provided as a list of pairs, such as 2 3 -4 -2
where 2 3 is the first pair and -4 -2 is the next one.
The first number of the pair is the row coordinate R and the second one
is the column coordinate C.

You need to follow a path from R to C and sum up all the values you encounter
in cells. For example, with coordinates 2 3 you start from the beginning of the
2nd row and move towards the 3rd column. When you reach the column,
you go up because the column coordinate 3 is positive.

With coordinates -4 -2 you start from the end of the 4th row (because -4 is negative)
and move towards the 2nd column. When you reach it, you go down (-2 is negative).

Check the following picture for a clearer idea.

table

The path 2 3 yields a sum of 17 which is higher than the sum you obtain
by following -4 -2 (15)

Print the maximum sum you find to the standard output.
Note

You always have to move horizontally in rows and vertically in columns. For example, in the above picture, the correct path with coordinates -4 -2 is 3 -> 2 -> 5 -> 3 -> 2 and NOT 3 -> 4 -> 3 -> 6 -> 2.
Input
    On the first line, you receive an integer N - the number of rows in the matrix
    On the next N lines, each row of the matrix is given, with columns separated by a space
    On the last line, the R and C coordinates are given, separated by spaces

Output
    On the only line of output, print the maximum sum found.

Constraints
    N will be an integer between 5 and 20, inclusive.
    All rows have the exact same length, also between 5 and 20, inclusive.
    The R and C coordinates will always be valid and inside the matrix.
    The R C pairs will be at least 1 and no more than 20.
    Matrix elements will have values in range -5000 and 5000.

Sample Tests
Input

6
1 2 3 4 5 6
2 3 4 5 6 7
6 5 4 3 2 1
3 4 5 6 7 8
4 5 6 7 8 9
9 8 7 6 5 4
3 5 3 -5 -4 -2

Output
43

Input
5
1 22 3 41 5 2
2 13 4 -5 6 5
-6 5 9 31 2 8
3 14 5 -6 7 4
4 -5 6 -7 8 7
-3 -3 3 3 4 -3 -4 3

Output
61


Input
5
1 2 3 4 5
3 6 5 3 2
5 6 7 3 5
5 3 5 2 3
7 2 6 3 4
2 3 -4 -2

Output
17
"""


matrix = []

rows = int(input())
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

coordinates = [int(x) for x in input().split()]
couples = []
temp = []
sum_list = []

for idx in range(0, len(coordinates), 2):
    temp.append(coordinates[idx])
    temp.append(coordinates[idx + 1])
    couples.append(temp)
    temp = []

for current_couple in couples:
    row = current_couple[0]
    row_coord = current_couple[0]
    if row_coord > 0:
        row_coord -= 1
    else:
        row_coord = abs(row_coord) - 1

    col = current_couple[1]
    col_coord = current_couple[1]
    if col_coord > 0:
        col_coord -= 1
    else:
        col_coord = abs(col_coord) - 1

    counter = 0
    if row > 0:
        for idx in range(0, col_coord + 1):
            counter += matrix[row_coord][idx]
    else:
        for idx in range(len(matrix[0]) - 1, col_coord, - 1):
            counter += matrix[row_coord][idx]

    if col > 0:
        for idx in range(0, row_coord):
            counter += matrix[idx][col_coord]
    else:
        for idx in range(rows - 1, row_coord - 1, - 1):
            result = matrix[idx][col_coord]
            counter += result
    sum_list.append(counter)


print(max(sum_list))

