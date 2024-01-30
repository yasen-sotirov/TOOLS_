
def sum_range(range_end):
    return 1 if range_end == 1 else range_end + sum_range(range_end - 1)


        # върни 5 + нещо
        # нещото е == 4 + нещо
        # нещото е == 3 + нещо
        # нещото е == 2 + нещо
        # нещото е == 1

print(sum_range(6))
