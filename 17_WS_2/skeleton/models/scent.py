class Scent:
    lavender = "lavender"
    vanilla = "vanilla"
    rose = "rose"

    @classmethod
    def from_string(cls, scent_string):
        if scent_string not in [cls.lavender, cls.vanilla, cls.rose]:
            raise ValueError(f"None of the possible Scent values matches "
                             f"the value {scent_string}.'")
