# def  count_digits(digits):
#     if not digits:
#         return 0
#
#     return 1 + count_digits(digits[1:])
#
# print(count_digits("54321"))



def count_numbers(numbers):
    if numbers < 10:
        return 1

    # маха по една цифра докато не стане == една цифра
    return 1 + count_numbers(numbers // 10)

print(count_numbers(123456))