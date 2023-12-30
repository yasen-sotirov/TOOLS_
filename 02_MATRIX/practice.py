"PRACTISE"   #matrix

"CREATE EMPTY RECTANGULAR MATRIX"
def empty_rectangular_matrix(rows: int, cols: int):
    matrix = [[0] * cols for _ in range(rows)]
    return matrix

rows, cols = [int(el) for el in input('type number for rows and cols: ').split()]
print(empty_rectangular_matrix(rows, cols))




"CREATE EMPTY SQUARE MATRIX"
def square_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    return matrix

print(square_matrix(int(input('type matrix size: '))))



