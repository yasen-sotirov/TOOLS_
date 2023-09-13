
def even_sum(range_num):
    if range_num < 2:
        return 0

    if range_num % 2 != 0:
        return even_sum(range_num - 1)
    else:
        return range_num + even_sum(range_num - 1)

        # върни 6 + нещо
        # нещото е == 4 + нещо
        # нещото е == 2 + нещо
        # нещото е == 0


print(even_sum(6))