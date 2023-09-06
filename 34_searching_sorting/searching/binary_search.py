
def binary_search_rec(t, nums, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if nums[mid] < t:
        return binary_search_rec(t, nums, mid + 1, end)
    elif nums[mid] > t:
        return binary_search_rec(t, nums, start, mid - 1)
    else:
        return mid


def binary_search_iter(t, nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < t:
            start = mid + 1
        elif nums[mid] > t:
            end = mid - 1
        else:
            return mid

    return -1


nums = [6, 8, 9, 11, 14, 17, 22, 23, 25, 28, 30]
# print(binary_search_rec(6, nums, 0, len(nums) - 1))
# print(binary_search_rec(11, nums, 0, len(nums) - 1))
# print(binary_search_rec(30, nums, 0, len(nums) - 1))
# print(binary_search_rec(15, nums, 0, len(nums) - 1))
# print()
print(binary_search_iter(6, nums))
print(binary_search_iter(11, nums))
print(binary_search_iter(30, nums))
print(binary_search_iter(15, nums))
