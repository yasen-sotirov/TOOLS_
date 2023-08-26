def reverse(str):
    if len(str) <= 1:
        return str

    return f'{reverse(str[1:])}{str[0]}'


print(reverse('Recursion ftw!'))
