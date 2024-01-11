"""
Longest Block in String
A block in a string is a run of adjacent chars that are the same.
Given a string, return the first substring that is with the length of the largest
"block" in the string.

Input
Read from the standard input:
    string to search in -> hoopla

Output
Print to the standard output:
    One line of output - the first block with maximum lenght in the given array -> oo
    please note that different case matters.

Sample Tests
Input
hoopa

Output
oo

Input
abbCCCcddBBBxx

Output
CCC
"""

string = input()
# ней–голям елемент
max_block = ""
# работен блок
temp_block = ""

# обхождам стринга елемент по елемент
for el in string:
    # ако елемента е равен на последния елемент в работния блок
    if el == temp_block[-1:]:
        # добавям елемента към работния блок
        temp_block += el
    else:
        # ако са различни проверявам дали работния блок е по-голям от най-големия блок
        if len(temp_block) > len(max_block):
            # ако е по-голпм приравнявам най-големия на работния
            max_block = temp_block
        # и започвам да пълня нанов работния блок с последния различен елемент
        temp_block = el

# проверявам дали последния блок е по-голям
if len(temp_block) > len(max_block):
    max_block = temp_block

print(max_block)
