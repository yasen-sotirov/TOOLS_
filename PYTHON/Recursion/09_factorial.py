"ФАКТОРИАЛ"     # Факториал на дадено число е произведението
# (умножението) от всички положителни цели числа, <= на него
# 5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))



"ИТЕРАТИВНО"
def counter_factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n

    return result

print(counter_factorial(5))