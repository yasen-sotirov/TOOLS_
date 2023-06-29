# scope resolution example 
# Ask students - what will the console output be
# Discuss why

x = 2
print(x)

def outer_func():
    print(x)
    def inner_func():
        print(x)

    inner_func()


outer_func()

# uncomment this before the demo
# inner_func() 
