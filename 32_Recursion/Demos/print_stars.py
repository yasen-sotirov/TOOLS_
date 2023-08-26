def rec_print_diamond(height, n = 1):
    stars = '*' * n

    if n == height:
        # middle row
        print(stars)
        return

    offset = ' ' * ((height - n) // 2)

    # top half
    print(f'{offset}{stars}')

    rec_print_diamond(height, n + 2)

    # bottom half
    print(f'{offset}{stars}')


rec_print_diamond(11)
