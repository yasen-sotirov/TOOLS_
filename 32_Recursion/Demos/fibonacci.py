
def fibonacci_slow(n):
    if n <= 2:
        return 1

    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


def fibonacci_with_memo(n, memo={}):
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    nth_fibo = (
        fibonacci_with_memo(n - 1, memo) +
        fibonacci_with_memo(n - 2, memo))
    memo[n] = nth_fibo

    return nth_fibo


print(fibonacci_with_memo(35))
print(fibonacci_slow(35))
