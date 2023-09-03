import sys

sys.setrecursionlimit(2 ** 16)

rows, cols = map(int, input().split())

coins = [[int(x) for x in input().split()] for _ in range(rows)]

r, c = next((i, row.index(0)) for i, row in enumerate(coins) if 0 in row)


def neighbours(r, c):
    left = coins[r][c - 1] if c > 0 else 0

    right = coins[r][c + 1] if c < cols - 1 else 0

    up = coins[r - 1][c] if r > 0 else 0

    down = coins[r + 1][c] if r < rows - 1 else 0

    return left, right, up, down


def collect(r, c):
    left, right, up, down = neighbours(r, c)

    best = max(left, right, up, down)

    if best == 0:
        return 0

    coins[r][c] -= 1

    if best == left:
        return 1 + collect(r, c - 1)

    if best == right:
        return 1 + collect(r, c + 1)

    if best == up:
        return 1 + collect(r - 1, c)

    if best == down:
        return 1 + collect(r + 1, c)


print(collect(r, c))