"""Factorial 5! = 5-4-3-2-1 = 120
Given n of 1 or more, return the factorial of n,
which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
"""

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))