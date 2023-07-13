from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class BoardItem:
    def __init__(self, title: str, due_date: date):
        if len(title) < 5 or len(title) > 30:
            raise ValueError('Illegal title length  (5:30 char)')
        if due_date < date.today():
            raise ValueError("Due date can't be in the past.")
        self._title = title
        self._due_date = due_date
        self._status = ItemStatus.OPEN
        self.logs = []
        description = f"Item created: {self.info()}"
        log = EventLog(description)
        self.logs.append(log)

    def revert_status(self):
        description = f"Changed status: from {self.status} to {ItemStatus.previous(self.status)}"
        log = EventLog(description)
        self.logs.append(log)
        self._status = ItemStatus.previous(self.status)

    def advance_status(self):
        description = f"Changed status: from {self.status} to {ItemStatus.next(self.status)}"
        log = EventLog(description)
        self.logs.append(log)
        self._status = ItemStatus.next(self._status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'

    @property
    def status(self):
        return self._status

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        old_due_date = self._due_date
        if value < date.today():
            raise ValueError('Due date can not be in the past.')
        else:
            if value != self._due_date:
                description = f"DueDate changed from {old_due_date} to {self._due_date}"
                log = EventLog(description)
                self.logs.append(log)

    @property
    def title(self):
        # връща състоянието
        return self._title

    @title.setter
    def title(self, new_title):
        # задава ново състояние
        old_title = self._title
        if len(new_title) < 5 or len(new_title) > 30:
            raise ValueError('Illegal title length  (5:30 char)')
        self._title = new_title
        result = f"Title changed from {old_title} to {self._title}"

    def history(self) -> str:
        history_as_str = ""
        for log in self.logs:
            history_as_str += log.info() + "\n"
        history_as_str += "\n--------------\n"
        return history_as_str

