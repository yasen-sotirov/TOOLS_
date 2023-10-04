
def count_occurrences(words: list) -> dict:
    tracker = {}

    for word in words:
        if word in tracker:
            tracker[word] += 1
        else:
            tracker[word] = 1

    return tracker


def two_sum(numbers: list, target_sum: int) -> tuple:
    seen = {}

    for i in range(len(numbers)):
        target = target_sum - numbers[i]
        if target in seen:
            return (seen[target], i)
        else:
            seen[numbers[i]] = i

    return (-1, -1)


def special_coins(coins: str, catalogue: str) -> int:
    catalogue = set(catalogue)
    special = 0

    for coin in coins:
        if coin in catalogue:
            special += 1

    return special


def are_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_dict = {}
    s2_dict = {}

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 not in s1_dict:
            s1_dict[char1] = char2

        if char2 not in s2_dict:
            s2_dict[char2] = char1

        if (s1_dict[char1] != char2 or s2_dict[char2] != char1):
            return False

    return True
