from custom_exceptions import RoomNumberNotValid, RoomAlreadyBooked


class Hotel:

    def __init__(self, name: str, rooms_count: int):
        self._name = name
        self._rooms: list[int] = [0 for _ in range(rooms_count)]
        # 0 - free, 1 - booked

    @property
    def capacity(self):
        return self._rooms.count(0)

    @property
    def room_count(self):
        return len(self._rooms)

    @property
    def name(self):
        return self._name

    def get_room_status(self, room_num:int):
        if not self._is_room_number_valid(room_num):
            raise ValueError()
        return self._rooms[room_num-1]

    def book_room(self, room_num):
        if not self._is_room_number_valid(room_num):
            raise RoomNumberNotValid()

        if self._rooms[room_num-1] == 1:
            raise RoomAlreadyBooked()

        self._rooms[room_num - 1] = 1

    def _is_room_number_valid(self, room_num):
        return not any([room_num <= 0, room_num > len(self._rooms)])



hotel_1 = Hotel("Central", 20)
print(hotel_1.name)
print(hotel_1.room_count)
print(hotel_1.capacity)

hotel_1.book_room(1)
hotel_1.get_room_status(1)

print(hotel_1.name)
print(hotel_1.room_count)
print(hotel_1.capacity)