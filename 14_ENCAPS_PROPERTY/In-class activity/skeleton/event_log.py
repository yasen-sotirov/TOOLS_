from datetime import datetime


class EventLog:

    def __init__(self, description: str):
        if len(description) < 5 or len(description) > 30:
            raise ValueError('Illegal description length  (5:30 char)')
        self._description: str = description
        self._timestamp = datetime.now()

    @property
    def description(self):
        return self._description

    @property  # getter - получава инфо за обекта
    def timestamp(self):
        return self._timestamp

    def info(self):
        formatted_datetime = self._timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        return f"[{formatted_datetime}] {self._description}"
