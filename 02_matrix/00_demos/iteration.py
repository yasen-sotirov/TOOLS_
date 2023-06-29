list_2d = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for sublist in list_2d:
    for el in sublist:
        print(el, end='')
    print()

for r in range(len(list_2d)):
    for c in range(len(list_2d[r])):
        el = list_2d[r][c]
        print(f'[{r}][{c}] = {el}')