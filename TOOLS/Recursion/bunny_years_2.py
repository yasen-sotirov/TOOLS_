


def bunny_2(num, memo={1: 2, 2:5, 3:7}):

    if num in memo:
        return memo[num]

    memo[num] = 5 + bunny_2(num - 2, memo)
    return memo[num]

print(bunny_2(50))