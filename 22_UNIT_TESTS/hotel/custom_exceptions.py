class RoomNumberNotValid(Exception):
    def __init__(self):
        super().__init__("Room number is not valid")


class RoomAlreadyBooked(Exception):
    def __init__(self):
        super().__init__("Room is not available")
