from datetime import date, timedelta
from board import Board
from board_item import BoardItem


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = BoardItem('Refactor this mess', add_days_to_now(2))
item.due_date += timedelta(days=365 * 2)  # two years in the future
item.title = 'Not that important'
item.revert_status()
item.advance_status()
item.revert_status()
# print(item.history())
