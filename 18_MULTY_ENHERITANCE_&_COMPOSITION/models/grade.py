class BaseGrade:
    def display(self):
        raise NotImplemented("Override")

class LetterGrade:
    _ALLOWED_GRADE = ["A", "B", "C", "D", "E"]

    def __init__(self, grade: str) -> None:
        if grade not in LetterGrade._ALLOWED_GRADE:
            raise ValueError("error")
        self._grade = grade

    @property
    def grade(self):
        return self._grade


class NumericGrade:

    def __init__(self, grade: int) -> None:
        if grade < 0 or grade > 100:
            raise ValueError("error")
        self._grade = grade

    @property
    def grade(self):
        return self._grade