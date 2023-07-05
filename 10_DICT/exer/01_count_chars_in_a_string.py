"""
1.	Count Chars in a String
Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"

Examples
Input
text

Output
t -> 2
e -> 1
x -> 1

Input
text text text
Output
t -> 6
e -> 3
x -> 3
"""


data = input()
counter = {}

# итерирам през стринга
for char in data:
    if not char == " ":
        if char not in counter:
        # ако го няма го добавям
            counter[char] = 0
        # ако го има го събирам
        counter[char] += 1

    elif char == " ":
        # не изпълнявам текущата итерация
        continue

for key, value in counter.items():
    print(f"{key} -> {value}")
