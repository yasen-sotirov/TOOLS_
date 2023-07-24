from datetime import date, timedelta
from board import Board
from issue import Issue
from task import Task


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = Issue('Refactor this mess', 'Mnogo e zle', add_days_to_now(2))
anotherItem = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
issue.advance_status()
issue.due_date += timedelta(days = 1)
print(issue.history())

task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

for board_item in [issue, task]:
    print(board_item.info())
