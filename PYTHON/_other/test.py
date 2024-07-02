'''
write me a python program to sort integers by btoy repetitions of each number
if they are even, let the greater number appear first
[1,5,3,2,4,32,5,3,5,3,6,7,5,3,1,45]
To return: [5,5,5,5,5,3,3,3,3,3,1,1,45,32,7,6,4,2]
'''


#
# from collections import Counter
#
# def sort_integers_by_frequency(numbers):
#     # Count the frequency of each number
#     counts = Counter(numbers)
#
#     # Sort numbers based on frequency (descending) and value (ascending)
#     sorted_numbers = sorted(numbers, key=lambda x: (-counts[x], x%2, x))
#
#     return sorted_numbers
#
# # Example usage:
# numbers = [1, 5, 3, 2, 4, 32, 5, 3, 5, 3, 6, 7, 5, 3, 1, 45]
# sorted_numbers = sort_integers_by_frequency(numbers)
# print(sorted_numbers)


def custom_sort(lst):
    # Create a dictionary to count occurrences of each number
    count = {}
    for num in lst:
        if num not in count:
            count[num] = 0
        count[num] += 1

    # Sort the numbers based on the count of repetitions
    # For even numbers, sort them in descending order
    sorted_lst = sorted(lst, key=lambda x: (-count[x], x % 2 == 0, -x))

    return sorted_lst

# Test the function
lst = [1, 5, 3, 2, 4, 32, 5, 3, 5, 3, 6, 7, 5, 3, 1, 45]
sorted_lst = custom_sort(lst)
print(sorted_lst)
