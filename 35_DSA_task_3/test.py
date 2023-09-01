def find_duplicates_recursive(lst, index1=0, index2=1, duplicates=[]):
    if index1 == len(lst) - 1:
        return duplicates

    if index2 == len(lst):
        return find_duplicates_recursive(lst, index1 + 1, index1 + 2, duplicates)

    if lst[index1] == lst[index2]:
        duplicates.append((lst[index1], lst[index2]))

    return find_duplicates_recursive(lst, index1, index2 + 1, duplicates)

# Пример на използване
my_list = [1, 2, 2, 3, 4, 4, 5]
duplicate_pairs = find_duplicates_recursive(my_list)
print(duplicate_pairs)
