"""2. Write a function that 'merges' two equal length numbers.
The merging operation adds the digits that are in the same positions and
if the result is greater than 9, only the last digit remains. So 1 + 2 = 3,
but 8 + 5 = 3 also.

x = merge(123, 123) # x = 246
x = merge(789, 123) # x = 802 (7 + 1 = 8, 8 + 2 = 10, 9 + 3 = 12)"""


def merge_two_numbers(num_1, num_2):
    num_1 = [int(x) for x in num_1]
    num_2 = [int(x) for x in num_2]

    index = 0
    result = ''

    for el in range(len(num_1)):
        current_num = num_1[index] + num_2[index]
        if current_num > 9:
            current_num_as_str = str(current_num)
            current_num = current_num_as_str[-1]
        result += "".join(str(current_num))
        index += 1

    return result


first_num, second_num = input().split(", ")
merged_result = merge_two_numbers(first_num, second_num)
print(merged_result)
