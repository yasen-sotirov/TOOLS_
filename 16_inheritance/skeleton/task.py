from datetime import date
from board_item import BoardItem


class Task(BoardItem):

    def __init__(self, title: str, due_date: date, assignee= "Person"):
        super().__init__(title, due_date)
        self.assignee = assignee

    @property
    def assignee(self):
        return self.assignee

    @assignee.setter
    def assignee(self, name):
        pass