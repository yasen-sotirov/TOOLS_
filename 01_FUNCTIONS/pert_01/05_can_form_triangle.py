"""
5. Write a function that determines if three numbers (representing lengths of sides)
can form a triangle. To form a triangle the largest side must be smaller
than the sum of the other two. You do not know which of the three parameters
will be the largest.

x = can_form_triangle(3,4,5) # x = True
x = can_form_triangle(3,6,3) # x = False
"""


def can_form_triangle(el_1, el_2, el_3):
    lst = [el_1, el_2, el_3]
    max_element = max(lst)
    lst.remove(max_element)
    if max_element >= lst[0] + lst[1]:
        return False
    return True


# x = can_form_triangle(3,4,5)   # x = True
x = can_form_triangle(3,6,3)   # x = False
print(x)