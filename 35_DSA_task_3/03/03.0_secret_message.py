"""
Input
a2{bc2{d}e}fj

    Output
abcddebcddefj
"""

from collections import deque



def flatten(sequence):
    open_stack = []
    close_queue = deque()
    multiplier = 1
    output = []

    for ind in range(len(sequence)):
        el = sequence[ind]
        if el == "{":
            open_stack.append(ind)
        elif el == "}":
            close_queue.append(ind)

    open_par = open_stack.pop()
    close_par = close_queue.popleft()
    current_str = sequence[open_par + 1:close_par]

    for el in current_str:
        if el.isnumeric():
            multiplier = int(el)
        elif el.isinstance(el, str):
            output.append(el)
        else:
            output.extend(flatten(current_str))
    return output


input_str = "a2{bc2{d}e}fj"
print(flatten(input_str))