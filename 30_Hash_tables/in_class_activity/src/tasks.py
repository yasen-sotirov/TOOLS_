
def count_occurrences(words: list) -> dict:
    dictionary = {}
    for el in words:
        if el not in dictionary.keys():
            dictionary[el] = 0
        dictionary[el] += 1
    return dictionary



# def two_sum(numbers: list, target_sum: int) -> tuple:
#     for i1 in range(1, len(numbers)):
#         if numbers[i1] + numbers[0] == target_sum:
#                 return 0, i1
#         for i2 in range(i1 - 1, 0, - 1):
#             if numbers[i1] + numbers[i2] == target_sum:
#                 return i2, i1
#     return - 1, - 1

def two_sum(numbers: list, target_sum: int) -> tuple:
    dictionary = {}
    for index, num_1 in enumerate(numbers):
        num_2 = target_sum - num_1
        if num_2 in dictionary:
            # връща индекса на търсения ключ
            return dictionary[num_2], index
        dictionary[num_1] = index
    return -1, -1

# num, target = [1, 2, 3], 5            # (1, 2)
# num, target = [2, 0, 1, 3, 2], 4      # (1, 3)
# num, target = [2, 0, 1, 4, 2], 4      # (2, 3)
num, target = [2, 0, 1, 5, 2], 4      # (2, 3)
print(two_sum(num, target))





def special_coins(coins: str, catalogue: str) -> int:
    # dictionary = {}
    # for el in catalogue:
    #     if el not in dictionary.keys():
    #         dictionary[el] = 0
    # for el in coins:
    #     if el in dictionary.keys():
    #         dictionary[el] += 1
    # return sum(dictionary.values())

    catalogue = set(catalogue)
    counter = 0
    for el in coins:
        if el in catalogue:
            counter += 1
    return counter



def are_isomorphic(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    dictionary = {}
    for i in range(len(str1)):
        char1, char2 = str1[i], str2[i]
        # Проверява дали ключа вече го има
        if char1 in dictionary.keys():
            # ако го има, проверява дали е равен на вече зададената стойност
            if dictionary[char1] != char2:
                # ако не отговаря, значи преди сме въвели друга комбинация
                return False
        else:
            # Проверяваме дали текущия символ от str2 не е вече закачен към друг ключ
            if char2 in dictionary.values():
                return False
            dictionary[char1] = char2
    return True


# s1, s2 = 'theeyes', 'theysee'
# s1, s2 = 'theeyes', '1233435'
# s1, s2 = 'theeyes', '1234533'
# print(are_isomorphic(s1, s2))


