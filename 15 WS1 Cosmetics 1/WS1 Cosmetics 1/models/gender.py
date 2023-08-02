class Gender:
    # константи
    MEN = 'Men'
    WOMEN = 'Women'
    UNISEX = 'Unisex'

    @classmethod
    def from_string(cls, gender_string):
        # проверява дали поаденото съвпада с наличните класове
        if gender_string not in [cls.MEN, cls.WOMEN, cls.UNISEX]:
            raise ValueError(
                f'None of the possible Gender values matches the value {gender_string}.')

        return gender_string
