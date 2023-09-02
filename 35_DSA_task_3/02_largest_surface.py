"""
    Largest Surface
Write a program that finds the largest possible sequence of equal neighboring elements in a rectangular matrix
and prints its size.

Input
    On the first line you will receive the numbers N and M separated by a single space;
    On the next N lines there will be M numbers separated with spaces - the elements of the matrix;

Output
    Print the size of the largest area of equal neighboring elements
Constraints
    3 <= N, M <= 1024

    Input
5 6
1 3 2 2 2 4
3 3 3 2 4 4
4 3 1 2 3 3
4 3 1 3 3 1
4 3 3 3 1 1

    Output
13

    Input
3 3
1 1 1
2 1 2
2 2 2

5

Hint: you can use the algorithm Depth-first search or Breadth-first search.
"""



def inside(row_pos, col_pos):
    if 0 <= row_pos < rows and 0 <= col_pos < cols:
        return True
    return False


def has_neighbors(row_pos, col_pos, pos_num):
    p_neighbors = []
    if inside(row_pos, col_pos - 1) and pos_num == matrix[row_pos][col_pos - 1]:    # left
        p_neighbors.append((row_pos, col_pos - 1))
    if inside(row_pos, col_pos + 1) and pos_num == matrix[row_pos][col_pos + 1]:    # right
        p_neighbors.append((row_pos, col_pos + 1))
    if inside(row_pos - 1, col_pos) and pos_num == matrix[row_pos - 1][col_pos]:    # up
        p_neighbors.append((row_pos - 1, col_pos))
    if inside(row_pos + 1, col_pos) and pos_num == matrix[row_pos + 1][col_pos]:    # down
        p_neighbors.append((row_pos + 1, col_pos))

    return p_neighbors[0] if p_neighbors else False



rows, cols = map(int, input().split())
matrix = []
areas = []

for row in range(rows):
    col = [int(el) for el in input().split()]
    matrix.append(col)

areas.append({(0, 1) : matrix[0][1]})

# обхожда полето
for row_ind in range(rows):
    for col_ind in range(cols):
        current_position = (row_ind, col_ind)
        position_num = matrix[row_ind][col_ind]
        # взема потенциалните съседи
        has_neighbor = has_neighbors(row_ind, col_ind, position_num)

        if not has_neighbor:
            areas.append({(row_ind, col_ind): position_num})
        else:
            for index, field_dict in enumerate(areas):
                neighborhood_num = max(field_dict.values())
                # neighborhood_num = areas[index][has_neighbor]
                if neighborhood_num == position_num:
                    areas[index][row_ind, col_ind] = position_num
                else:
                    areas.append({(row_ind, col_ind): position_num})


max_neighborhood = 0

for n_dict in areas:
    count = len(n_dict)
    if count > max_neighborhood:
        max_neighborhood = count


print(max_neighborhood)

