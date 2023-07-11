
def split_tuple(the_tuple, splitter):
    prev_split_idx = 0
    tuples = []
    for idx, val in enumerate(the_tuple):
        if val == splitter:
            tuples.append(the_tuple[prev_split_idx: idx])
            prev_split_idx = idx + 1

    tuples.append(the_tuple[prev_split_idx:])
    return tuples


def merge_tuples(first_tuple, second_tuple):
    larger = max(len(first_tuple), len(second_tuple))
    output = []
    for idx in range(larger):
        a = first_tuple[idx] if idx < len(first_tuple) else None
        b = second_tuple[idx] if idx < len(second_tuple) else None
        output.append((a, b))

    return output


def sum_tuples(first_tuple, second_tuple):
    larger = max(len(first_tuple), len(second_tuple))
    output = ()
    for idx in range(larger):
        a = first_tuple[idx] if idx < len(first_tuple) else 0
        b = second_tuple[idx] if idx < len(second_tuple) else 0
        output += (a+b,)

    return output


def sum_tuple_with(the_tuple, number):
    output = ()
    for val in the_tuple:
        output += (val + number,)

    return output


def contains_subtuple(sub_tuple, the_tuple):
    sub_len = len(sub_tuple)
    max_idx = len(the_tuple) - sub_len + 1

    for i in range(max_idx):
        if the_tuple[i: sub_len+i] == sub_tuple:
            return True

    return False


def delete_subtuple(sub_tuple, the_tuple):
    sub_len = len(sub_tuple)
    max_idx = len(the_tuple) - sub_len + 1

    for i in range(max_idx):
        if the_tuple[i: sub_len+i] == sub_tuple:
            return the_tuple[:i] + the_tuple[sub_len+i:]

    return the_tuple


def subtuple_index(sub_tuple, the_tuple):
    sub_len = len(sub_tuple)
    max_idx = len(the_tuple) - sub_len + 1

    for i in range(max_idx):
        if the_tuple[i: sub_len+i] == sub_tuple:
            return i

    return -1


def insert_subtuple(sub_tuple, the_tuple, index):
    if index < 0 or index > len(the_tuple):
        return the_tuple
    else:
        left = the_tuple[:index]
        right = the_tuple[index:]

        return left + sub_tuple + right


def concat_tuples(*tuples):
    output = ()
    for t in tuples:
        output += t

    return output


def replace_subtuple(sub_tuple, new_sub_tuple, the_tuple):
    sub_len = len(sub_tuple)
    max_idx = len(the_tuple) - sub_len + 1

    for i in range(max_idx):
        if the_tuple[i: sub_len+i] == sub_tuple:
            return the_tuple[:i] + new_sub_tuple + the_tuple[sub_len+i:]

    return the_tuple
