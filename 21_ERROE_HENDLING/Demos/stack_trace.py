def parse_number(n):
    return int(n)

def read_number():
    value = input() # enter 'txt'
    return parse_number(value)

num = read_number()
print(num)