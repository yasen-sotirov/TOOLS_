"""
Spiral Matrix
    Write a program that reads from the console a positive integer number N
(1 ≤ N ≤ 20) and prints a matrix holding the numbers from 1 to N*N in the form
of square spiral like in the examples below.
Input
    The input will always consist of a single line containing a single number - N.

Output
    Spiral matrix as described below.

Constraints
    N will always be a valid integer number.
    1 ≤ N ≤ 20

Sample tests
Input
2

Output
1 2
4 3

Input
3

Output
1 2 3
8 9 4
7 6 5

Input
4

Output
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""


size_matrix = int(input())
# създавам празна матрица по размер
matrix = [[0] * size_matrix for _ in range(size_matrix)]
counter = 1

# определям граници на обхождане
row_start = 0
row_end = size_matrix - 1
col_start = 0
col_end = size_matrix - 1

# задавам цикъл който да приключи до най-голямото възможно число, което size_matrix*size_matrix
while counter <= size_matrix * size_matrix:
    # обхождам матрицата надясно и
    for idx in range(col_start, col_end + 1):
        matrix[row_start][idx] = counter
        counter += 1
    row_start += 1      # ред +1 за да не се застъпя с предното


    # обхождам надолу от нов ред до ред + 1 защото ренджа е ексклузив
    for idx in range(row_start, row_end + 1):
        matrix[idx][col_end] = counter
        counter += 1
    # кпоследната колона вече са пълни затова изместваме границата наляво с 1
    col_end -= 1

    # обхождам наляво до границата -1 щото ренджа е ексклузив и реално стигаме до самата граница
    for idx in range(col_end, col_start - 1, - 1):
        matrix[row_end][idx] = counter
        counter += 1
    # последният ред вече е пълен затова измествам границата нагоре с единица
    row_end -= 1

    # обхождам нагоре
    for idx in range(row_end, row_start - 1, - 1):
        matrix[idx][col_start] = counter
        counter += 1
    col_start += 1

# принтиране на матрицата
for row in matrix:
    print(" ".join(str(el) for el in row))



