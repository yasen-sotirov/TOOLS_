
from math import log2


def merge_sort(arr: list[int], left_index: int, right_index: int):
    if left_index < right_index:
        # 'divide' - the log2 part in O(n *log2(n))
        mid_index = (left_index + right_index) // 2
        merge_sort(arr, left_index, mid_index)
        merge_sort(arr, mid_index + 1, right_index)

        # 'conquer'
        merge(arr, left_index, mid_index, right_index)


def merge(arr: list[int], start_index: int, mid_index: int, end_index: int):
    # this additional array leads to O(n) space
    merge_arr: list[int] = [None] * (end_index - start_index + 1)

    left_index = start_index
    right_index = mid_index + 1
    merge_index = 0

    # merge both
    while left_index <= mid_index and right_index <= end_index:
        if arr[left_index] < arr[right_index]:
            merge_arr[merge_index] = arr[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = arr[right_index]
            right_index += 1

        merge_index += 1

    # check for trailing elements from left subarray
    while left_index <= mid_index:
        merge_arr[merge_index] = arr[left_index]
        left_index += 1
        merge_index += 1

    # check for trailing elements from right subarray
    while right_index <= end_index:
        merge_arr[merge_index] = arr[right_index]
        right_index += 1
        merge_index += 1

    # copy back sorted run of elements
    for i in range(len(merge_arr)):
        arr[start_index + i] = merge_arr[i]


arr = [8, 0, 9, 1, 4, 3, 2, 5, 7, 6, 0, 5, 1, 9, 3,
       4, 2, 8, 7, 6, 0, 8, 9, 1, 4, 3, 2, 5, 7, 6, 0, 9]
merge_sort(arr, 0, len(arr) - 1)

print(arr)
