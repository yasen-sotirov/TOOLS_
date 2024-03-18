# this quicksort is not that quick - too many intermediate lists are created
# but easier to comprehend
def quick_sort(nums):
    if nums == []:
        return []

    pivot = nums[-1]
    smaller = [n for n in nums[:-1] if n <= pivot]
    larger = [n for n in nums if n > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


nums = [1,2,3,1,2,3,1,2,3]
sorted = quick_sort(nums)
print(sorted)
