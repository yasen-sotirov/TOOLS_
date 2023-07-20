from board import Board
from board_item import BoardItem
from item_status import ItemStatus


class User:

    def __init__(self, username: str, email: str, assigned_tasks: list):
        if username in Board.all_users:
            raise ValueError(f"The username already exist!")
        self._username = username
        self.email = email
        self._assigned_tasks: list[ItemStatus] = []
        self._capacity = 0

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, new_email):
        if "@" not in self.email:
            raise ValueError("The email address must have '@'!")
        self.email = new_email

    @property
    def assigned_tasks(self):
        return self._assigned_tasks

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self, value):
        self.capacity = 3

    def advance_task_status(BoardItem, advanced):
        pass

    def receive_task(self):
        pass

    def remove_task(self):
        pass




