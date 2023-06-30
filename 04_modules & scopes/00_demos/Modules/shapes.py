# import more than one name from a module - 'pi' value and 'pow' function
from math import pi, pow

def circle_area(radius):
    return pi * pow(radius, 2)

def rectangle_area(width, height):
    return width * height