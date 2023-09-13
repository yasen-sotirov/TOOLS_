"""
Sum Digits
Write a program that reads a four-digit number and
displays the sum of its digits

    1213 => 1 + 2 + 1 + 3 = 7
    2346 => 2 + 3 + 4 + 6 = 15
"""

def sum_digits(nums):
    if nums == "":
        return 0
    # събира първия елемент със сумата на останалите

    return int(nums[0]) + sum_digits(nums[1:])

n = input()
print(sum_digits(n))