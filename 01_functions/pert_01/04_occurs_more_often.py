"""
4. Write a function that returns the letter which occurs more often
than another letter in a text. Use the function from the previous exercise.

x = stronger_letter('abca', 'a', 'b') # x = 'a'
x = stronger_letter('abbca', 'c', 'b') # x = 'b'
x = stronger_letter('aabbc', 'b', 'a') # x = 'b'
(return the first one in case of a tie)
"""


def occurrences(searched_el, line):
    counter = 0
    for current_el in line:
        if searched_el == current_el:
            counter += 1
    return counter


def stronger_letter(line, el_1, el_2):
    count_el_1 = occurrences(el_1, line)
    count_el_2 = occurrences(el_2, line)
    if count_el_1 >= count_el_2:
        return el_1
    return el_2


x = stronger_letter('abca', 'a', 'b') # x = 'a'
# x = stronger_letter('abbca', 'c', 'b') # x = 'b'
# x = stronger_letter('aabbc', 'b', 'a') # x = 'b' (return the first one in case of a tie)
print(x)