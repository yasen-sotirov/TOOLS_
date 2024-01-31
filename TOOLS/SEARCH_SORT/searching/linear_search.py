def find_index_linear(t, nums):
    for i in range(len(nums)):
        if t == nums[i]:
            return i
    return -1


nums = [11, 23, 8, 14, 30, 9, 6, 17, 22, 28]
print(find_index_linear(14, nums))
print(find_index_linear(15, nums))