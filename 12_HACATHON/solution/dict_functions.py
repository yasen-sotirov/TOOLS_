
def from_string(the_string, *, pair_sep=',', kv_sep='=', value_type='str'):
    my_dict = {}
    for pair in the_string.split(pair_sep):
        key, value = pair.split(kv_sep)
        if value_type == 'int':
            my_dict[key] = int(value)
        elif value_type == 'float':
            my_dict[key] = float(value)
        else:
            my_dict[key] = value

    return my_dict


def aggregate(data):
    my_dict = {}
    for k, v in data:
        if k in my_dict:
            my_dict[k].append(v)
        else:
            my_dict[k] = [v]

    return my_dict


def aggregate_min(data):
    my_dict = {}
    for k, v in data:
        if k in my_dict:
            my_dict[k] = min(my_dict[k], v)
        else:
            my_dict[k] = v

    return my_dict


def aggregate_max(data):
    my_dict = {}
    for k, v in data:
        if k in my_dict:
            my_dict[k] = max(my_dict[k], v)
        else:
            my_dict[k] = v

    return my_dict


def aggregate_sorted(data, *, reverse=False):
    my_dict = {}
    for k, v in aggregate(data).items():
        my_dict[k] = sorted(v, reverse=reverse)

    return my_dict


def aggregate_avg(data):
    my_dict = {}
    for k, v in aggregate(data).items():
        my_dict[k] = sum(v) / (len(v) or 1)

    return my_dict


def aggregate_sum(data):
    my_dict = {}
    for k, v in data:
        if k in my_dict:
            my_dict[k] += v
        else:
            my_dict[k] = v

    return my_dict


def aggregate_count(data):
    my_dict = {}
    for k, v in data:
        if k in my_dict:
            my_dict[k] += 1
        else:
            my_dict[k] = 1

    return my_dict


def with_keys(the_dict, keyset):
    my_dict = {}
    for key in keyset:
        if key in the_dict:
            my_dict[key] = the_dict[key]

    return my_dict


def exclude_keys(the_dict, keyset):
    my_dict = {}
    for key in the_dict.keys():
        if key not in keyset:
            my_dict[key] = the_dict[key]

    return my_dict


def dicts_union_preserve(first_dict, second_dict):
    my_dict = {}
    for k, v in first_dict.items():
        my_dict[k] = [v]

    for k, v in second_dict.items():
        if k in my_dict:
            my_dict[k].append(v)
        else:
            my_dict[k] = [v]

    return my_dict


def dicts_union_override(first_dict, second_dict):
    my_dict = {}
    for k, v in first_dict.items():
        my_dict[k] = v

    for k, v in second_dict.items():
        my_dict[k] = v

    return my_dict


def dicts_symmetric_difference(first_dict, second_dict):
    my_dict = {}
    for k, v in first_dict.items():
        my_dict[k] = v

    for k, v in second_dict.items():
        if k in my_dict:
            del my_dict[k]
        else:
            my_dict[k] = v

    return my_dict


def dicts_difference(first_dict, second_dict):
    my_dict = {}
    for k, v in first_dict.items():
        if k not in second_dict:
            my_dict[k] = v

    return my_dict


def dicts_intersection(first_dict, second_dict):
    my_dict = {}
    for k, v in first_dict.items():
        if k in second_dict:
            my_dict[k] = [v, second_dict[k]]

    return my_dict


def dict_flatten(the_dict):
    my_list = []
    for v in the_dict.values():
        my_list.extend(v)

    return my_list


def dict_keysort(the_dict):
    return sorted(the_dict.items(), key=lambda t: t[0])


def dict_valuesort(the_dict):
    return sorted(the_dict.items(), key=lambda t: t[1])
