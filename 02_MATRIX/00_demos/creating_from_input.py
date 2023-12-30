# how can we read input like this:
# 2 3 (first line: rows, cols)
# 1 (element at [0][0])
# 3
# 5
# 2 (element at [1][0])
# 4
# 6

# rows, cols = input().split()
#
# list_2d = []
# for r in range(int(rows)):
#     new_sublist = []
#     for c in range(int(cols)):
#         next_element = int(input())
#         new_sublist.append(next_element)
#     list_2d.append(new_sublist)
#
# print(list_2d)





# read input formatted like this:
# 3 4 (rows, cols)
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6

rows, cols = input().split()     # meaning of underscore -> ignore the second element

matrix = []
for cols in range(int(rows)):
    matrix.append(input().split())

# will contain non-parsed numbers
# you might need to parse them depending on the scenario
print(matrix)
