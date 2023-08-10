numbers = [42, 31, 20, 53, 64]


def between_20_and_50(x):
    return x >= 20 and x <= 50


# filter is a built-in higher-order func
filtered = filter(between_20_and_50, numbers)

print(list(filtered))

# higher-order function -> function that returns another function
def between(min, max):
    def inner_func(x):
        return x >= min and x <= max

    return inner_func


filtered = filter(between(40, 50), numbers)
print(list(filtered))


# 'map' built-in higher-order func
names = ['steVen', 'JACK', 'aliCE']
capitalized = map(str.capitalize, names)
print(list(capitalized))
