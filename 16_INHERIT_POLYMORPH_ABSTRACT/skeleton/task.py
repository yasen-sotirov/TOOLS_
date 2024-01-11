from datetime import date
from board_item import BoardItem
from item_status import ItemStatus


class Task(BoardItem):

    def __init__(self, title: str, assignee, due_date: date):
        super().__init__(title, due_date)
        self.assignee = assignee
        self._status = ItemStatus.TODO

    @property
    def assignee(self):
        return self.assignee

    @assignee.setter
    def assignee(self, name):
        if len(name) < 5 or len(name) > 30:
            raise ValueError(f"The task name must be [5:30] char")
        self.assignee = name

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value):
        value = BoardItem.status


task = Task('Test the application flow', 'Steven', add_days_to_now(2))
print(task.title)      # Test the application flow
print(task.due_date)   # 2022-03-18
print(task.status)
print(task.assignee)   # Steven