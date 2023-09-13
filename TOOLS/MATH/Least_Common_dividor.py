# най–малко общо кратно
# https://www.w3resource.com/python-exercises/python-basic-exercise-32.php

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0):
            result = z
            break
        z += 1

    return result


num_1 = int(input())
num_2 = int(input())
print(lcm(num_1, num_2))






# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Function to return LCM of two numbers
def lcm(a, b):
    return (a // gcd(a, b)) * b


# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))