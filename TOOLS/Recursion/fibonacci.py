"""
Fibonacci
The Fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition.
The first two values in the sequence are 0 and 1 (essentially 2 base cases).
Each subsequent value is the sum of the previous two values, so the whole sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n)
method that returns the nth Fibonacci number, with n=0 representing the start of the sequence.
"""
from functools import lru_cache

# @ lru_cache(maxsize=None)
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
# print(fibonacci(8))


def fibonacci_memo(num, memo={0:0, 1:1, 2:1}):
    if num in memo.keys():
        return memo[num]

    memo[num] = fibonacci_memo(num - 1, memo) + fibonacci_memo(num - 2, memo)
    return memo[num]

print(fibonacci_memo(8))