"КОЛКО УШИ ИМАТ N-бр ЗАЙЦИ"    #
# def bunny_ears(bunny: int):
#     if bunny <= 1:
#         return 2
#
#     return 2 + bunny_ears(bunny - 1)
# #   бр уши ^     брой зайци^
#
# print(bunny_ears(5))

'''
При извикване на bunny_ears(5), стъпките ще бъдат следните:

    bunny_ears(5) връща 2 + bunny_ears(4)
    bunny_ears(4) връща 2 + bunny_ears(3)
    bunny_ears(3) връща 2 + bunny_ears(2)
    bunny_ears(2) връща 2 + bunny_ears(1)
    bunny_ears(1) връща 2.

При bunny <= 1, започваме да "разгъваме" рекурсията
като за всеки заек добавяме по 2 уши

    bunny_ears(1) връща 2
    bunny_ears(2) връща 2 + 2 = 4   
    bunny_ears(3) връща 2 + 4 = 6
    bunny_ears(4) връща 2 + 6 = 8
    bunny_ears(5) връща 2 + 8 = 10
'''


"РЪЧНА ОПТИМИЗАЦИЯ"
def bunny_memo(num, memo={}):
    if num <= 1: return 2

    if num in memo:
        return memo[num]

    bunny_num = 2 + bunny_memo(num - 1, memo)

    memo[num] = bunny_num
    return bunny_num

print(bunny_memo(10))


"ВАРИАНТ С ЗАЙЦИ С 2+3 УШИ"
# тогава дъното ще е два заека с общо 5 уши
# и ще намаляваме броя зайци с по 2, не с по 1.

# def bunny_2_3(num, memo={}):
#     if num == 2:
#         return 5
#
#     if num in memo:
#         return memo[num]
#
#     bunny = 5 + bunny_2_3(num - 2, memo)
#     #    уши^      бр зайци^    памет^
#     memo[num] = bunny
#
#     return bunny

# или:  memo[num] = 5 + bunny_2_3(num - 2, memo)
#       return memo[num]