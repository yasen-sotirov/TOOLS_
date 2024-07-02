"СЪБИРА ЧЕТНИТЕ ЧИСЛА ОТ 0 до N"   #

def even_sum(range_num):
    if range_num < 2:       # защото под 2 няма други четни
        return 0

    if range_num % 2 != 0:
        return even_sum(range_num - 1)  #  ако е нечетно само сваля надолу
    else:
        return range_num + even_sum(range_num - 1)

print(even_sum(6))

'''
върни 6 + нещо
нещото е == 4 + нещо
нещото е == 2 + нещо
нещото е == 0

= 2 + 0 = 2
= 4 + 2 = 6
= 6 + 6 = 12
'''



