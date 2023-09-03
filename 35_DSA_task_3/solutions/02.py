rows, cols = map(int, input().split())

matrix = [[None] + input().split() + [None] for _ in range(rows)]

none_row = [[None] * (cols + 2)]

matrix = none_row + matrix + none_row

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))


def explore(x, y, val):
    matrix[x][y] = None

    return 1 + sum(explore(x + dx, y + dy, val)

                   for dx, dy in dirs

                   if matrix[x + dx][y + dy] == val)


best = max(explore(r, c, matrix[r][c])

           for r in range(rows)

           for c in range(cols)

           if matrix[r][c] is not None)

print(best)