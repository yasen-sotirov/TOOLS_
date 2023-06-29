# scope resolution example 
# Ask students - what will the console output be
# Discuss why

x = 2

def outer_func():
    x = 3
    print(x)
    def inner_func():
        x = 4
        print(x)

    inner_func()
    print(x)

print(x)
outer_func()
print(x)
