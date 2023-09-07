"""
Bunny Ears
We have a number of bunnies and each bunny has two big floppy ears.
We want to compute the total number of ears across all the bunnies
recursively (without loops or multiplication).
"""

def bunny_years(bunny):
    # if bunny <= 1:
    #     return 2
    # return 2 + bunny_years(bunny - 1)
    return 2 if bunny <= 1 else 2 + bunny_years(bunny -1)


print(bunny_years(8))