"""
Power N
Given base and n that are both 1 or more,
compute recursively (no loops) the value of base to the n power,
 so powerN(3, 2) is 9 (3 squared).


 Например, ако въведете base = 2 и power = 3, функцията power_n ще се извика по следния начин:

    power_n(2, 3) -> не е базов случай, затова извикваме power_n(2, 2)
    power_n(2, 2) -> не е базов случай, затова извикваме power_n(2, 1)
    power_n(2, 1) -> не е базов случай, затова извикваме power_n(2, 0)
    power_n(2, 0) -> това е базовият случай, връща 1

След това рекурсията се разгръща обратно:

    power_n(2, 0) връща 1.
    power_n(2, 1) изчислява 2 * 1 и връща 2.
    power_n(2, 2) изчислява 2 * 2 и връща 4.
    power_n(2, 4) изчислява 2 * 4 и връща 8.

Така функцията намира резултата от 2 на трета степен, който е 8, и го извежда на екрана.
"""


def power_n(_base, _power):
    if _power == 0:
        return 1

    # умножава резултата (2 * дъното) Power брой пъти
    bottom = power_n(_base, _power - 1)
    return _base * bottom


base = int(input())
power = int(input())

print(power_n(base, power))