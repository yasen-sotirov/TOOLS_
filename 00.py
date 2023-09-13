# 1 <= 2
# връща всички числа от първото 5-8 = 5,6,7,8

def recursion(start, final, lst=[]):
    if start == final:
        lst.append(final)
        return lst

    lst.append(start)


    return recursion(start + 1, final, lst)


start = int(input())
final = int(input())

result = recursion(start, final)
print(result)
