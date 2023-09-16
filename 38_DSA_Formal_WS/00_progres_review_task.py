# 1 <= 2
# връща всички числа от първото 5-8 = 5,6,7,8

def recursion(start, final, lst=None):
    if lst is None:
        lst = []

    if start == final + 1:
        # lst.append(final)
        return lst

    lst.append(start)
    # започва от старта и добавя към него докато достигне финала
    return recursion(start + 1, final, lst)


# print(recursion(int(input()), int(input())))
print(recursion(5, 10))
