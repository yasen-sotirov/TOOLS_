"""
Three Groups
You are given an array of numbers.
Your task is to group the numbers by remainder of 3.

Example:
arr = {1, 2, 3, 4, 5, 6, 7}

groups:
0 -> 3, 6
1 -> 1, 4, 7
2 -> 2, 5

Input

Read from the standard input
    On the single line, read the numbers of the array
        Separated by a whitespace

Output
Print on the standard output

    On the first line, print the group with remainder 0
    On the second line, print the group with remainder 1
    On the third line, print the group with remainder 2
    On each line, the numbers in a group are separated with a single whitespace

Sample tests
Input

1 2 3 4 5 6 7

Output
3 6
1 4 7
2 5

Input
3 3 3 3 3

Output
3 3 3 3 3

Note that there are two empty lines for the two empty groups
"""


data_line = [int(x) for x in input().split()]
matrix = [[], [], []]

for num in data_line:
    if num % 3 == 0:
        matrix[0].append(num)
    elif num % 3 == 1:
        matrix[1].append(num)
    elif num % 3 == 2:
        matrix[2].append(num)

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
