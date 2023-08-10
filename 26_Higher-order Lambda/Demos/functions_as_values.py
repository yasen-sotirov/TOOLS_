def draw_line(width, symbol='-'):
    return symbol * width

# functions are values - they can be assigned to vars or stored in lists, 
# or anyway a 'normal' value can be used

result = draw_line(10)
func_reference = draw_line

print(result)
print(func_reference)
print(func_reference(15, '*'))

# list of functions
funcs = [draw_line, func_reference]

for func in funcs:
    line = func(20, '#')
    print(line)
