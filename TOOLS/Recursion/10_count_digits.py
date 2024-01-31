"БРОЙ ЦИФРИТЕ В ЧИСЛО"  #

def count_numbers(numbers):
    if numbers < 10:
        return 1

    # маха по една цифра докато не стане == една цифра
    return 1 + count_numbers(numbers // 10)

print(count_numbers(12345))

    # 5.  return 1 + нещо(12345 // 10)
    # 4.  return 1 + нещо(1234 // 10)
    # 3.  return 1 + нещо(123 // 10)
    # 2.  return 1 + нещо(12 // 10)
    # 1.  нещо == 1
    # 2.  return 1 + 1
    # 3.  return 1 + 2
    # 4.  return 1 + 3
    # 5.  return 1 + 4


"ИТЕРАТИВНО"
# print(len(str(123456)))