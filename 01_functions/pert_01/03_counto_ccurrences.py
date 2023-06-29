""" 3. Write a function that counts the number of occurrences of a letter in a string.

x = occurrences('a', 'aaa') # x = 3
x = occurrences('a', 'aabb') # x = 2
x = occurrences('a', 'bbcc') # x = 0
"""


def occurrences(searched_el, line):
    counter = 0
    for current_el in line:
        if searched_el == current_el:
            counter += 1
    return counter


x = occurrences('a', 'aaa')
print(x)

