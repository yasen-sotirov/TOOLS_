"""
Dog Years
Most people believe that 1 human year (HY) equals 7 dog years (DY),
however, dogs reach adulthood in approximately 2 human years.
So it's better to count the first two HY as 10 DY each and then count
the remaining HY as 4 DY each.
Write a program that correctly converts human years (HY) to dog years (DY).
You may need some form of conditional logic.
Input
    On the first line, you will receive HY - the number of human years.

Output
    On the only line of output, print DY - the number of dog years.
Constraints
    1 <= HY <= 15

Input
2

Output
20

Input
4

Output
28

"""

r = int(input())
c = int(input())

for row in range(r):
    for col in range(c):
        print("*", end="")
