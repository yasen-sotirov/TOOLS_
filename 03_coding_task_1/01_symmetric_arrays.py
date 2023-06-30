"""
Symmetric Arrays

You are given some arrays of numbers. Your task is to check if they are symmetric.
A symmetric array is one, where the element at index x is equal to the element
at index array.length - 1 - x.

Input
Read from the standard input.
    On the first line, read the number N - the number of arrays to follow.
    On the N lines, read the elements of each array, separated by white space.

Output
Print to the standard output.
    For each of the arrays, print Yes of the array is symmetric, or No if it's not.

Sample tests
Input
4
1 2 3 2 1
2 1
1 2 2 1
4

Output
Yes
No
Yes
Yes
"""

array_num = int(input())

for _ in range(array_num):
    current_array = [int(el) for el in input().split()]
    if len(current_array) == 1:
        print("Yes")

    else:
        first_part = current_array
        second_part = current_array[::-1]
        if first_part == second_part:
            print("Yes")
        else:
            print("No")

    # else:
    #     index = 0
    #     is_symmetric = True
    #     for num in range(len(current_array) // 2):
    #         if current_array[index] == current_array[-index-1]:
    #             index += 1
    #         else:
    #             is_symmetric = False
    #     if is_symmetric:
    #         print("Yes")
    #     else:
    #         print("No")

