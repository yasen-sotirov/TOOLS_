"""
Given a non-negative int n, compute recursively (no loops) the count of the occurrences
of 8 as a digit, except that an 8 with another 8 immediately to its left counts double,
so 8818 yields 4.

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""

def count_oc(nums):
    if not nums:
        return 0
    first, *rest = nums

    if not rest:
        return int(first == "8")

    if first == "8" and rest[0] == "8":
        return 2 + count_oc(rest)
    if first == "8":
        return 1 + count_oc(rest)

    return count_oc(rest)

print(count_oc(list(input())))