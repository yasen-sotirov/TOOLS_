def reverse_str(array):
    if array == "":
        return ""

    last_el = array[-1]
    return last_el + reverse_str(array[:-1])

print(reverse_str("abc"))



