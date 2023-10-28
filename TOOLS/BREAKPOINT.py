"BREAKPOINT FUNCTION"  #

"""
h - help
w - where
n - next
s - step (step into function)
c - continue
p - print
l - list
q - quit
j - jump on line
tbreak - temporary breakpoint
"""

def my_func():
    x = 5
    y = 6
    print(x + y)
    return x + y

breakpoint()

a = int(0.1)
b = 1.0
c = a + b

# breakpoint()

e = 0.1
f = 1.0
g = e + f
xy = my_func()

# breakpoint()

print('done')



