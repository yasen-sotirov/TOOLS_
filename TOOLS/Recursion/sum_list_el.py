
def sum_list_el(num_list):
    if not num_list:
        return 0

    else:
        # get_num минава през всеки елемент и се опитва да го събере с нещо
        # когато стигне дъното започва да го събира с 0
        get_num = num_list[0]
        bottom = sum_list_el(num_list[1:])
        result = get_num + bottom
        return result

        # върни 1 + нещо
        # нещото е == 2 + нещо
        # нещото е == 3 + нещо
        # нещото е == 4 + нещо
        # нещото е == 5 + нещо
        # нещото е == 0

nums = [1, 2, 3, 4, 5]
print(sum_list_el(nums))
