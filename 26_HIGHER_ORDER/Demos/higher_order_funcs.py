def usa_law(age):
    return age > 21

def europe_law(age):
    return age > 18

def bulgaria_law(age):
    return True

# a higher-order function
def is_allowed_to_drink(age, filter_func):
    if filter_func(age):
        print('Welcome to the bar')
    else:
        print('Back off, punk')


# the higher-order functions are a technique for achieving abstraction
is_allowed_to_drink(14, bulgaria_law)
is_allowed_to_drink(14, usa_law)