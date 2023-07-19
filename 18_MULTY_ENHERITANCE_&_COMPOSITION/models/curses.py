class Course:
    def __init__(self, name: str) -> None:
        self._name = name
        self._students: list[Student]

        self._department_courses: list[Course]

    @property
    def name(self):
        return self._name
