"NUMBERS"  #

num_1, num_2, num_3 = 1, 2, 3
num_4, num_5, num_6 = 10, 2.5, 123

"ЦЕЛОЧИСЛЕНО ДЕЛЕН"     # колко пъти делим без остатък
# print(7 // 2)   # 3
# print(12 // 3)  # 4
# print(13 // 3)  # 4


"МОДУЛНО ДЕЛЕНЕ"    # остатъкът от целочисленото делене
# print(7 % 2)    # 1
# print(12 % 3)   # 0
# print(13 % 3)   # 1


"НАЙ-МАЛКО, НАЙ-ГОЛЯМО"
# print(min(num_1, num_2, num_3))
# print(max(num_1, num_2, num_3))


"MAX/MIN SIZE ЧИСЛО"
# import sys
# print(sys.maxsize)
# print(-sys.maxsize)


"СЛАГА ЗАПЕТАЯ МЕЖДУ НУЛИТЕ НА ГОЛЕМИ ЧИСЛА"
# num = 1000000
# print(f"{num:,}")


"ЗАКРЪГЛЯ FLOAT РЕЗУЛТАТ СЛЕД ЗАПЕТАЯТА"
# num_as_float = num_3 / num_2
# print("{:.5f}".format(num_as_float))    # 1.50000
# num = 3.1415926
# print(f'{num:.2f}')     # 3.14
# print(f'{num:+.2f}')    # +3.14
# print(round(num, 3))    # 3.142


"СЛАГА НУЛИ ПРЕД ЧИСЛОТО"
# print(f"{num_3:03d}")   # 003
# print(f"{num_4:03d}")   # 010
# print(f"{num_6:03d}")   # 123


"ПРЕОБРАЗУВА В ПРОЦЕНТИ"
# num = 0.35
# print(f"{num:.2%}") # 35.00%


"ЗАКРЪГЛЯВА НАГОРЕ, НАДОУ"
# from math import ceil, floor
# number = 1.618
# print(ceil(number))     # 2
# print(floor(number))    # 1


"ЧАСОВЕ И МИНУТИ"
hour = int(input())
minutes = int(input())
hour += minutes // 60
minutes %= 60
if hour > 23:
    hour = 0
print(f'{hour}:{minutes:02d} ч')

minutes = int(input())
h = minutes // 60
m = minutes % 60
print(f'{h}:{m:02d} ч')


"ПРОСТО ЧИСЛО"
number = int(input())
is_dividable = False

for i in range(2, number):
    if (number % i) == 0:
        is_dividable = True
        break

if is_dividable:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")




