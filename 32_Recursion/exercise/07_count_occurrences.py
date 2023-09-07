"""
Given a non-negative int n, return the count of the occurrences of 7 as a digit,
so for example 717 yields 2. (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""

def count_occurrences(num):
    if not num:
        return 0

    if num[0] == "7":
        # 1 ще я добави към резултата, който в дъното ще е 0
        return 1 + count_occurrences(num[1:])
    return count_occurrences(num[1:])

n = input()
print(count_occurrences(n))