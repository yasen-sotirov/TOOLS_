import curses
import grade


class Student:
    def __init__(self, name: str):
        self._name = name
        self._grade: list[int] = []
        self._courses: list[Course] = []

    @property
    def name(self):
        return self._name