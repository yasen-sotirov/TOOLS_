"""
Given an array of ints, compute recursively if the array contains a 6.
We'll use the convention of considering only the part of the array
that begins at the given index. In this way, a recursive call can pass
index+1 to move down the array. The initial call will pass in index as 0.
"""

def array_with(data):
    if not data: return False

    return data[0] == 6 or array_with(data[1:])


d = [int(el) for el in input().split(",")]
index = int(input())
print(str(array_with(d[index:])).lower())

# 1,3,4,5,6,2
# 0