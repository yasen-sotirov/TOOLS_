

def partition(nums, start, end):
    pivot = nums[(start + end) // 2]

    while start <= end:
        # find index of the next element smaller than the pivot element
        while nums[start] < pivot:
            start = start + 1

        # find index of the next element larger than the pivot element
        while nums[end] > pivot:
            end = end - 1

        # there might be no need for swapping
        if start <= end:
            # move smaller element to the left of pivot
            # larger element to the right
            nums[start], nums[end] = nums[end], nums[start]

            start = start + 1
            end = end - 1

    # this is the index where the pivot element currently is
    return start

def quick_sort(nums, start, end):
    if start < end:
        pivot_index = partition(nums, start, end)
        quick_sort(nums, start, pivot_index - 1)
        quick_sort(nums, pivot_index, end)

nums = [11, 23, 8, 14, 30, 9, 6, 17, 22, 28]
quick_sort(nums, 0, len(nums) - 1)
print(nums)