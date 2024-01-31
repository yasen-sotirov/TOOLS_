"""
Triangle
We have triangle made of blocks. The topmost row has 1 block,
the next row down has 2 blocks, the next row has 3 blocks, and so on.
Compute recursively (no loops or multiplication) the total number of blocks
in such a triangle with the given number of rows.
"""

def triangle(rows):
    if rows == 0:
        return 0

    # бр блокове на ред == № на реда
    # връщаме блоковете на този ред + блоковете от предходния ред
    return rows + triangle(rows - 1)
    #     = 5^    +       нещо^

print(triangle(5))

'''
= 5 + нещо
= 4 + нещо
= 3 + нещо 
= 2 + нещо
= 1 + нещо
нещото = 0

= 1 + 0
= 2 + 1
= 3 + 3
= 4 + 6
= 5 + 10 = 15
'''