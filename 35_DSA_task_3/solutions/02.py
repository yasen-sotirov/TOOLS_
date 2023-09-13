rows, cols = map(int, input().split())
matrix = []
island_dict = {}

for row in range(rows):
    matrix.append([int(el) for el in input()])


visited = {(row, col): {(row, col)} for row in range(rows) for col in range(cols) if matrix[row][col]}

for (row, col) in list(visited):
    for next_r, next_c in [(row + 1, col), (row, col + 1)]:

        if (next_r, next_c) not in visited:
            continue

        if visited[row, col] == visited[next_r, next_c]:
            continue  # skip already merged

        visited[row, col].update(visited[next_r, next_c])  # Merge set of positions
        for (last_r, last_c) in visited[next_r, next_c]:
            visited[last_r, last_c] = visited[row, col]  # Propagate merged set to all


final = sorted(list(set(map(len, visited.values()))), reverse=True)
for el in final:
    print(el)





# 5 10
# 1000000010
# 1111000011
# 1000000000
# 1100001000
# 1000011100


# 4 4
# 0000
# 0110
# 0110
# 0000
