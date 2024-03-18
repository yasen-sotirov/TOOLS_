# def count_hi(data):
#     if len(data) == 1:
#         return 0
#
#     if data[:2] == "hi":
#         return 1 + count_hi(data[2:])
#     return count_hi(data[1:])
#
# print(count_hi(input()))


def count_letter(data, memo=[]):
    if not data:
        return 0

    if data[0] not in memo:
        memo.append(data[0])
        return count_letter(data[1:], memo)
    return 1 + count_letter(data[1:], memo)


print(count_letter((input())))