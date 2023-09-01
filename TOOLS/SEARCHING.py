"ТЪРСЕЩИ  АЛГОРИТМИ"   #
# Sequential - последователни: for el in num_list:
# Interval - интервани: работят с подредени масиви

nums = [6, 8, 9, 11, 14, 17, 22, 23, 25, 28, 30]



"БИНАРНО ТЪРСЕНЕ"   # log search, ще върне индекса на търсеното число
def binary_search_iter(target, num_list: list[int]):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid_ind = (start + end) // 2
        if num_list[mid_ind] > target:
            end = mid_ind - 1
        elif num_list[mid_ind] < target:
            start = mid_ind + 1
        else:
            return mid_ind
    return "Number not found"
print(binary_search_iter(6, nums))



def binary_search_rec(target, num_list, start, end):
    if start > end:
        return "Number not found"

    mid_ind = (start + end) // 2
    if num_list[mid_ind] < target:
        return binary_search_rec(target, num_list, mid_ind + 1, end)
    elif num_list[mid_ind] > target:
        return binary_search_rec(target, num_list, start, mid_ind - 1)
    else:
        return mid_ind
print(binary_search_rec(6, nums, 0, len(nums) - 1))










