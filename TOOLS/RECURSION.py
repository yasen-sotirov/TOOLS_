"РЕКУРСИЯ"   # да ревърснеш стринг рекурсивно
#  линейни и с разклинения


# def print_num(max_num):
#     if max_num == 0:
#         return
#     print_num(max_num - 1)
#     print(max_num)     # ако сложим принта вътре ще смени реда


# =========================
# def print_num(max_num):
#     if max_num != 0:
#         print_num(max_num - 1)
#         print(max_num)
#
# print_num(5)
# 1
# 2
# 3
# 4
# 5

"STRING REVERSE"
# "abcdef" -> "fedcba"

# def reverse_recursive(string):
#     if string == "":
#         return ''
#
#     last = string[-1]
#     the_rest_reserved = reverse_recursive(string[:-1])
#     return  last + the_rest_reserved
#
# reverse_recursive("abc")
# 'abcd' -> 'dcba'
# 'd' + 'cba'
#       // 'c' + 'ba'
#              // 'b' + 'a'
#                     // 'a' = reverse('')



# =========================
# def reverse_recursive(s):
#     if s == "":
#         return ''
#     return reverse_recursive(s[1:]) + s[0]
#
# the_result = reverse_recursive("abc")
# print(the_result)




"С РАКЛОНЕНИЯ"

# пример с данни в странен формат

# values = [1, 2, [3, 4], 5, [6]]

# def flatten(lst):
#     output = []
#     for x in lst:
#         if isinstance(x, int):
#             output.append(x)
#         else:
#             output.extend(x)
#     return output
#
# values2 = flatten(values)
# print(values2)

"FLATTEN ИЗРАВНЯВАНЕ" # рекурсия с разклонения
# values = [1, [2, [[[3, [4, [5, [6]]]], 7], 8], 9]]
#
# def flatten(lst):
#     output = []
#     for x in lst:
#         if isinstance(x, int):
#             output.append(x)
#         else:
#             output.extend(flatten(x))
#     return output
#
# values2 = flatten(values)
# print(values2)


"ЛАБИРИНТ"      # рекурсия с 4 разклоненя
lab = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0]
]

rows = len(lab)
cols = len(lab[0])

# 0,0  1,0  1,1  1,2  2,2  3,2  3,1

for r in range(rows):
    for c in range(cols):
        if lab[r][c] == 1:
            print(r,c)
