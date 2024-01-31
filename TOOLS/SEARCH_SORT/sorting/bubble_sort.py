def bubble_sort(nums):
    ordered = False
    while not ordered:
        # possible optimization for sorted lists
        ordered = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                ordered = False

nums = [11, 23, 8, 14, 30, 9, 6, 17, 22, 28]
bubble_sort(nums)
print(nums)