def sum_rec(nums):
    if nums == []:
        return 0

    first, *rest = nums

    return first + sum_rec(rest)


print(sum_rec([1, 2, 3, 4]))
print(sum_rec([-2]))
print(sum_rec([]))
