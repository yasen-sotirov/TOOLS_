# create 'use-once-and-forget' function with the lambda syntax sugar
# rewrite the examples from the other files

def is_allowed_to_drink(age, filter_func):
    if filter_func(age):
        print('Welcome to the bar')
    else:
        print('Back off, punk')

is_allowed_to_drink(14, lambda x: x >= 18)
is_allowed_to_drink(14, lambda x: x < 18)

numbers = [42, 31, 20, 53, 64]
print(list(filter(lambda x: x >= 20 and x <= 50, numbers)))
print(list(filter(lambda x: x >= 40 and x <= 50, numbers)))
print(list(filter(lambda x: x % 3 == 0, numbers)))

