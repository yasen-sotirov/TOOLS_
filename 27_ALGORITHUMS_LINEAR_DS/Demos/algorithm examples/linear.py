nums = [2, 5, 12, 7, 2, 4, 9, 8, 15, 21]


def search(nums, n):
    for num in nums:
        if n == num:
            return True

    return False


print('21?', search(nums, 21))
print('2?', search(nums, 2))
print('9?', search(nums, 9))
print('14?', search(nums, 14))
