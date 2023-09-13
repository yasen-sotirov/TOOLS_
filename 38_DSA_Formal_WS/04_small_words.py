def inside(row_pos, col_pos):
    if 0 <= row_pos < rows and 0 <= col_pos < cols:
        return True
    return False

def has_neighbor(r, c):
    neighbors = []

    if inside(r, c - 1) and matrix[r][c - 1] == 1:
        neighbors.append((r, c - 1))

    elif inside(r, c + 1) and matrix[r][c + 1] == 1:
        neighbors.append((r, c + 1))

    elif inside(r - 1, c) and matrix[r - 1][c] == 1:
        neighbors.append((r - 1, c))

    elif inside(r + 1, c) and matrix[r + 1][c] == 1:
        neighbors.append((r + 1, c))

    else:
        return False

    if neighbors:
        return neighbors



rows, cols = map(int, input().split())
matrix = []
island_dict = {}


for row in range(rows):
    matrix.append([int(el) for el in input()])

# обхожда полето
for r_ind in range(rows):
    for c_ind in range(cols):
        if matrix[r_ind][c_ind] == 1:
            island_dict[f"{r_ind}{c_ind}"] = [(r_ind, c_ind)]
        break
    break

for r_ind in range(rows):
    for c_ind in range(cols):
        neighbor = has_neighbor(r_ind, c_ind)

        if matrix[r_ind][c_ind] == 1 and neighbor:
            for key, value in island_dict.items():
                for v_el in value:
                    for n_el in neighbor:
                        if v_el == n_el:
                            island_dict[key] = value.append((r_ind, c_ind))


a = 5

print(matrix)