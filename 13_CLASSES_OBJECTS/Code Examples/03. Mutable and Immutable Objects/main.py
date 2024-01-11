# Numbers
x = 123
y = x

# changes to 'y' do no affect 'x'
y = y + 1
print(x, y)


# Strings
text1 = 'academy'
text2 = text1

# string methods never mutate the string object
text2.upper()
print(text1, text2)

# instead, they create a new string
upper_text = text2.upper()
print(upper_text)
print('id of academy:', id(text1), id(text2),
      id('academy'))  # all are the same
print('id of ACADEMY:', id(upper_text))  # not the same as previous

# Lists
my_list = [1,2,3]
my_list.append(4) # list is mutated (compare to string.upper() that create a new list)
print(my_list)

list_copy = my_list
list_copy.append(5)

# not really a copy:
print(my_list)
print(id(my_list), id(list_copy)) # same id == same object

# passing value to a function is the same as assigning it to a new variable
def change_immutable(x):
    x = x + 1

def change_mutable(lst):
    lst.append(5)

x1 = 10
change_immutable(x1)
print(x1) # still 10

lst1 = [1,2,3,4]
change_mutable(lst1)
print(lst1) # changed - 5 appended

