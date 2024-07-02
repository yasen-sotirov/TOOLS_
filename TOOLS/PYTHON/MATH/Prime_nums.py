def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


line = [1, 15, 2, 8, 31, 5, 9]
print(list(filter(lambda num: is_prime(num), line)))

