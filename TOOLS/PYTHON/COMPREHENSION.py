"""COMPREHENSION"""   # извадка

#        Output       Collection           Condition
sample = [x + 1    for x in range(5)     if x % 2 == 2]
#        Do this   for this collection  in this situation



number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
number_list_2 = [4, 8, 2, 6, 9]

# expresion = израз, който произвежда някаква стойност
# изразът се „композира“

# print([el ** 2 for el in number_list if el % 2 == 0])
#
# print(["even" if el % 2 == 0 else "odd" for el in number_list])

# всеки път когато не три трябва резултата от компрехеншъна, най-вероятно ти трябва for loop





"F-STRING COMPREHENSION"
# is_happy = True
# print(f"Ivan {'is' if is_happy else 'is not'} happy")


"TUPLE COMPREHENSION"
# print(("first", "second")[False])
# print(("first", "second")[True])


"ИМА ЛИ ГЛАВНА БУКВА"
# is_uppercase_presented = any([True for char in value if char.isupper()])

# all_users = [('pesho', 'qwe345!'), ('gosho', 'passwOrd1'), ('penka', '1a2b3c4d')]
# print([(user, password) for (user, password) in all_users if len(password) >= 8 and any(digit.islower() for digit in password) and any(digit.isupper() for digit in password) and any(digit.isnumeric() for digit in password)])



"ТЪРСИ ПО КЛЮЧОВА ДУМА"
# if search:
    # result = [p for p in result if (search.lower() in p.name.lower())]



"DEMO LIST COMPREHENSIONS"

# double all numbers
original = [1, 2, 3, 4]
doubled = [n * 2 for n in original]
print(original)
print(doubled)

# parse a list of strings
strings = ["11", "12", "13"]
integers = [int(n) for n in strings]
print(strings)
print(integers)

# or when you read from the console
integers = [int(n) for n in input().split(' ')]
print(integers)

# add a 'filtering' condition
evens = [n for n in integers if n % 2 == 0]
print(evens)

pizzas = {
    'pepperoni': 12.5,
    'sicilian': 17.0,
    'margheritta': 8.5
}

# try the alternative (list declaration + for loop + if condition approach)

cheap_pizzas = [name.capitalize() for name, price in pizzas.items() if price < 15.0]
print(cheap_pizzas)

# the same syntax also applies for sets
# [x for x in ...] - list comprehension
# {x for x in ...} - set comprehension




"DEMO DICT COMPREHENSIONS"

word = 'Hello, Telerik Academy!'

# dictionary comprehension
occurrences = {letter: word.count(letter) for letter in word}

for k, v in occurrences.items():
    print(f'{k} = {v}')


def avg(items):
    return sum(items) / len(items)


student_scores = {
    'Gosho': [4, 3, 2, 2, 4, 2],
    'Pesho': [3, 3, 2, 4, 5, 4],
    'Tosho': [6, 2, 6, 3, 2]
}

graduating_students = {
    name: avg(scores) for name, scores in student_scores.items() if avg(scores) > 3.0
}

print(graduating_students)
