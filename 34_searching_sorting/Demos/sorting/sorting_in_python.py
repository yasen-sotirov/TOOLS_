# sorting primitives

nums = [3, 1, 4, 2]
ordered_nums = sorted(nums)

print('Ordered', nums, '->', ordered_nums)

strings = ['cherry', 'banana', 'coffee', 'apple']
ordered_strings = sorted(strings)
print('Ordered', strings, '->', ordered_strings)
print('Reverse order of', strings, '->', sorted(strings, reverse=True))


# sorting user defined objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): return f'({self.name}, {self.age})'

    # used by the 'sorted' function
    def __lt__(self, other):
        return self.age < other.age


people = [Person('Peter', 40), Person('Louis', 38), Person('Meg', 16)]

print('Ordered by age ascending ->', *sorted(people))

print('Ordered by name descending ->',
      *sorted(people, key=lambda p: p.name, reverse=True))
