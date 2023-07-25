class BaseGrade:
    def display(self):
        raise NotImplemented("Override")

class LetterGrade(BaseGrade):
    _ALLOWED_GRADE = ["A", "B", "C", "D", "E"]

    def __init__(self, grade: str) -> None:
        if grade not in LetterGrade._ALLOWED_GRADE:
            raise ValueError("error")
        self._grade = grade

    @property
    def grade(self):
        return self._grade


class NumericGrade(BaseGrade):

    def __init__(self, grade: int) -> None:
        if grade < 0 or grade > 100:
            raise ValueError("error")
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    


class Course:
    def __init__(self, name: str) -> None:
        self._name = name
        self._students: list[Student]

        self._department_courses: list[Course]

    @property
    def name(self):
        return self._name



class Student:
    def __init__(self, name: str):
        self._name = name
        self._grade: list[int] = []
        self._courses: list[Course] = []

    def add_grade(self, grade: BaseGrade)
        

    @property
    def name(self):
        return self._name



student_1 = Student("Stamat")

grade_1 = LetterGrade("A+")
grade_2 = NumericGrade(78.3)
grade_3 = LetterGrade("B+")


student_1.add_grade
