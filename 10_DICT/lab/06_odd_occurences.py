"""
6.	Odd Occurrences
Write a program that prints all elements from a given sequence of words
that occur an odd number of times (case-insensitive) in it.

•	Words are given on a single line, space-separated.
•	Print the result elements in lowercase, in their order of appearance.
"""

data = input().split()
words = {}

# въвеждам данните в речника
for current_word in data:
    current_word = current_word.lower()
    # ako го няма го създавам, после го добавям
    if current_word not in words:
        words[current_word] = 0
    words[current_word] += 1

# обхождам речника
for key, value in words.items():
    if value % 2 != 0:
        print(key, end=" ")
