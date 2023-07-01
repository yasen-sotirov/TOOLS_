"""
Chess Square Color
Write a program that determines the color of a chessboard square based on its
Label and Rank

    Labels have values from a to h
    Ranks have values from 1 to 8

chessboard scheme
Input
    On the first line, you will receive L - the label
    On the second line, you will receive R - the rank

Output
    On the only line of output, print light or dark, based on your calculations
Constraints
    a <= L <= h
    1 <= R <= 8

Input
a
1

Output
dark

Input
f
3

Output
light

"""

label = input()
rank = int(input())

if label == "a" or label == "c" or label == "e" or label == "g":
    if rank % 2 == 1:
        print("dark")
    else:
        print('light')
else:
    if rank % 2 == 1:
        print("light")
    else:
        print("dark")
