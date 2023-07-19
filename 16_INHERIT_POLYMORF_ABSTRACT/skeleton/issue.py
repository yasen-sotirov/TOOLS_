from datetime import date
from board_item import BoardItem

class Issue(BoardItem):

    def __init__(self, title:str, description:str, dueDate:date):
        super().__init__()