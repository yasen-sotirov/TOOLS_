"""
Write a program that simulates the execution of n nested loops
from 1 to n which prints the values of all its iteration variables at any given time on a single line. Use recursion.
"""


def nested_loop(ind, arr):
    if ind >= len(arr):
        print(*arr, sep=" ")
        return

    for num in range(1, len(arr) + 1):
        arr[ind] = num
        nested_loop(ind + 1, arr)

n = int(input())
array = [None] * n
print(nested_loop(0, array))