def find_max(nums):
    if nums == []:
        raise ValueError('nums is empty')

    first, *rest = nums
    
    if rest == []:
        return first

    other = find_max(rest)

    return first if first > other else other 


print(find_max([1, 2, 3, 4]))
print(find_max([-2]))
print(find_max([]))
