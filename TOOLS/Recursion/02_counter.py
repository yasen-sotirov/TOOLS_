
def counter_func(number: int):
    if number <= 0:
        return 0

    counter_func(number - 1)
    print(number)

counter_func(int(input("type a number: ")))

'''
= 5-1
= 4-1
= 3-1
= 2-1
= 1-1 = 0, влиза в fi-a
започва да връща получените резултати
'''