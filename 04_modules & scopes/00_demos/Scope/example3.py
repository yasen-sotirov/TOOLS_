# Scope resolution example 
# Ask students - which function call will throw an error  
# a) both
# b) only first
# c) neither one 
# d) only second

def my_function():
    print(x)

my_function()
x = 42
my_function()
