list_2d = [
    [3, 2, 3],
    [4, 2, 4, 7],
    [6, 9]
]

# for sublist in list_2d:
#     for el in sublist:
#         print(el, end='')
#     print()
#
# for r in range(len(list_2d)):
#     for c in range(len(list_2d[r])):
#         el = list_2d[r][c]
#         print(f'[{r}][{c}] = {el}')

for row in range(len(list_2d)):
    for col in range(len(list_2d[row])):
        el = list_2d[row][col]
        print(f'[{row}][{col}] = {el}')
