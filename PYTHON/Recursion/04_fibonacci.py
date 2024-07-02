"ФИБОНАЧИ"  # в практиката се решава итеративно
# експоненциално нараства
# всеки елемент е равен на сумата от предишния с по-предишния елемент



def fibonacci_slow(num):
    if num <= 2:
        return 1

    return fibonacci_slow(num - 1) + fibonacci_slow(num - 2)

print(fibonacci_slow(8))    # връща 8то Фибоначи число



"РЪЧНА ОПТИМИЗАЦИЯ"
# мемоизация - алгоритъма се трансформира до линейна сложност
# всяко число се изчислява максимум веднъж.

def fibonacci_memo(num, memo={}):
    # определяне на дъното
    if num <= 2:
        return 1

    # проверка дали числото вече е изчислено
    if num in memo:
        return memo[num]

    # изчислява числото
    fibo_num = fibonacci_memo(num - 1, memo) + fibonacci_memo(num - 2, memo)
    # запазва го в речника
    memo[num] = fibo_num
    # извиква функцията отново
    return fibo_num

print(fibonacci_memo(8))



"ЗАВОДСКА ОПТИМИЗАЦИЯ"
from functools import lru_cache
# @ lru_cache(maxsize=None)
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
# print(fibonacci(8))

