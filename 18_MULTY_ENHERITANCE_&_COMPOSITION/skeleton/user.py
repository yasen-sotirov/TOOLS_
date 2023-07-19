from board import Board
from board_item import BoardItem


class User:

    def __init__(self, username: str, email: str, assigned_tasks: list):
        if username in Board.all_users:
            raise ValueError(f"The username already exist!")
        self._username = username
        self.email = email
        self.assigned_tasks = assigned_tasks

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

    def advance_task_status(self, task):
        prev = self._status
        self._status = ItemStatus.next(self._status)
        self._log_status_change(prev, self._status)


