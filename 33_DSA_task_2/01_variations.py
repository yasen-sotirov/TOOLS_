# task 01: Variations
"""
You are given the task to generate all possible variations of X and Y,
with length Z.

    On the first line, find the number Z
    On the second line, find the symbols X and Y

Output

    Print one variation on each line
        Ordered lexicographically

Input

3
o W

WWW
WWo
WoW
Woo
oWW
oWo
ooW
ooo

Input
4
9 1

Output
1111
1119
1191
1199
1911
1919
1991
1999
9111
9119
9191
9199
9911
9919
9991
9999
"""

def variations(string, symbols, length):
    # това което се променя в условието е дължината на възможната комбинация
    # затова връзвам дъното към нея
    if length == 0:
        variations_list.append(string)
        return

    for element in symbols:
        variations(string + element, symbols, length - 1)



variations_list = []
var_len = int(input())
el_1, el_2 = input().split()
variations("", el_1 + el_2, var_len)

variations_list.sort()

for el in variations_list:
    print(el)




# ========================================
# РЕШЕНИЕ ОТ САЙТА
n = int(input())
# sorting the two letters leads to generating sorted variations
# it's better to sort two letters than 2^n strings
a, b = sorted(input().split())

def variations(s):
    if len(s) == n:
        print(s)
    else:
        variations(s + a)
        variations(s + b)

variations('')




# ========================================
# РЕШЕНИЕ ОТ ЕДО
# вариациите са = 2^len
"""
max_len = int(input())
a, b = sorted(input().split())

def variations(string=""):
    if len(string) == max_len:
        print(string)
    else:
        variations(string + a)
        variations(string + b)

variations()
"""

