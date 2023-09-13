
def sum_range(range_end):
    if range_end == 1:
        return 1

    else:
        result = sum_range(range_end - 1)
        return result + range_end

        # върни 5 + нещо
        # нещото е == 4 + нещо
        # нещото е == 3 + нещо
        # нещото е == 2 + нещо
        # нещото е == 1

print(sum_range(5))
