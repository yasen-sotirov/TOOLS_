class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    def __init__(self):
        pass

    @classmethod
    def previous(cls, current):
        pass

    @classmethod
    def next(cls, current):
        pass



