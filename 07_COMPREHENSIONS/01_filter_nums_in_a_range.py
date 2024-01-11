"""
Write a list comprehension that filters all the numbers which are less than 5 or
larger than 15.

[1,15,2,8,31,5,9] -> [1,2,31]
"""

array = [1,15,2,8,31,5,9]
print([x for x in array if x < 5 or x > 15])
