# from board_item import BoardItem


class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    _order = (OPEN, TODO, IN_PROGRESS, DONE, VERIFIED)

    @classmethod
    def next(cls, current):
        idx = cls._order.index(current)
        # ако индекса е по-малък от 4 значи е преди края
        if idx < len(cls._order) - 1:
            new_status = cls._order[idx + 1]
            result = f"Status changed from {idx} to {new_status}"
            return result

        else:
            # ако е 4, значи е накрая
            return current

    @classmethod
    def previous(cls, current):
        # проверява къде се намира в момента
        idx = cls._order.index(current)
        # ако не е в началото се връща една стъпка назад
        if idx > 0:
            return cls._order[idx - 1]
        else:
            # ако е в началото, си остава там
            result = f"Cant change status, already at Open"
            return result
