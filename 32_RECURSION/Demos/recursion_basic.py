def rec_print(n):
    if n <= 0:
        # bottom case
        return

    # move after recursive call and examine results
    print(n)
    rec_print(n - 1)


rec_print(10)
