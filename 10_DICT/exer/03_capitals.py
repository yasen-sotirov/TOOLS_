"""
Using a dictionary comprehension, write a program that receives country names
on the first line, separated by comma and space ", ", and their corresponding
capital cities on the second line (again separated by comma and space ", ").

Print each country with their capital on a separate line in the following
format: "{country} -> {capital}". 
"""


country = input().split(", ")
capital = input().split(", ")

result = dict(zip(country, capital))

for key, value in result.items():
    print(f"{key} -> {value}")



def func(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    pass


