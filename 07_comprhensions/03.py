"""
Write a list comprehension that all the strings which are longer than 5 symbols.

['cat', 'dog', 'elephant', 'cucumber'] -> ['elephant', 'cucumber']
"""

lst = ['cat', 'dog', 'elephant', 'cucumber']
print([x for x in lst if len(x) > 5])
