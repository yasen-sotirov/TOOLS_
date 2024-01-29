def my_map(mapping_fn, collection):
    result_list = []
    for val in collection:
        # the essence of map - transform the val by using the supplied mapping_fn
        mapped_val = mapping_fn(val)
        result_list.append(mapped_val)

    return result_list


def my_filter(filtering_fn, collection):
    result_list = []
    for val in collection:
        # the essence of filter - only append to the list if the filtering_fn returns True
        if filtering_fn(val):
            result_list.append(val)

    return result_list


print('Plus one to [1, 2, 3]:', my_map(lambda x: x + 1, [1, 2, 3]))
# print('Only odd from [1, 2, 3]:', my_filter(lambda x: x % 2 == 1, [1, 2, 3]))
