"""
Bounce

You are given numbers N and M.
They form a matrix of the powers of 2.

Example: N = 3, M = 4

1 2 4 8
2 4 8 16
4 8 16 32

Starting from the top left corner of the matrix,
Go with diagonal moves, until you hit a wall.
When a wall is hit, change direction. You do this, until the direction cannot be changed, i.e. you hit a corner.

Example:
If you have the above matrix, the path will be: 1 4 16 16 4 4 4
"""


rows, cols = map(int, input().split())
total = 1
r, c, r_delta, c_delta = 1, 1, 1, 1

while r >= 0 and c >= 0 and r < rows and c < cols:
    total += 2 ** (r + c)

    if r == 0 or r == rows - 1:
        r_delta = -r_delta

    elif c == 0 or c == cols - 1:
        c_delta = -c_delta

    r += r_delta
    c += c_delta

print(total)