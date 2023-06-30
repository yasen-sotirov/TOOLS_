# LEGB

# LOCAL 
# both some_param and local_var are local to the function
def my_function(some_param):
    local_var = 5

    return local_var * some_param

## code "outside" the function can't access local variables
## print(some_param, local_var) 

# ENCLOSING
## nested_function() has access to its 'enclosing' scope - the local scope of the 'parent' function
def my_function(some_param):
    local_var = 5
    def nested_function():
        return local_var * some_param

    print(nested_function())

# GLOBAL
## This variable is available to all code inside the module
## it can be imported in other modules as `scopes.my_global_value`
my_global_value = 'Hello, scopes'

# BUILTINS
# functions like print(), min(), max(), sorted() are defined in the __builtins__ module. 
# It's available everywhere without importing


