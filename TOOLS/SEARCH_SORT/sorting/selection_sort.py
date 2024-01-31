def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i

        # search for the index of next minimum element
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j


        # swap the element at min_index with the current first element
        nums[min_index], nums[i] = nums[i], nums[min_index]


nums = [11, 23, 8, 14, 30, 9, 6, 17, 22, 28]
selection_sort(nums)
print(nums)