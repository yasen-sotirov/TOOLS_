list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(list_2d[1][1])
print(list_2d[2][2])

first_row = list_2d[0]
first_element = first_row[0]

# or
first_element = list_2d[0][0]

print(first_row)
print(first_row[0])
print(first_element)

list_2d[1] = [11, 12, 13]
print(list_2d)
list_2d[2][1] = 300
print(list_2d)

[
    [1, 2, 3], 
    [11, 12, 13], 
    [7, 300, 9]
]
