import time
import unittest

from custom_exceptions import RoomNumberNotValid, RoomAlreadyBooked
from hotel import Hotel


class Hotel_Should(unittest.TestCase):

    def setUp(self) -> None:
        """
        Arrange phase which will be present for each test scenario.
        """
        self.hotel = Hotel("Seaside", 5)
        self.start = time.time()

    def tearDown(self):
        self.end = time.time()
        print(self.end - self.start)

    def test_timeCounterWorksProperly(self):
        test_var = ["asd" for _ in range(100000)]
        self.assertEqual(["asd" for _ in range(100000)], test_var)

    def test_initializerSetsAttributes(self):
        name = "Seaside"

        self.assertEqual(name, self.hotel.name)
        self.assertEqual(5, self.hotel.room_count)
        self.assertIsInstance(self.hotel, Hotel)

    def test_nameIsReadonly(self):
        with self.assertRaises(AttributeError):
            self.hotel.name = "Bla"

    def test_capacity_returnsCorrectValue(self):
        self.assertEqual(5, self.hotel.capacity)

    def test_capacity_returnsCorrectValue_whenRoomsAreAvailable(self):
        self.hotel.book_room(1)

        self.assertEqual(4, self.hotel.capacity)

    def test_capacity_returnsCorrectValue_whenAllRoomsAreNotAvailable(self):
        hotel = Hotel("Seaside", 5)
        hotel.book_room(1)
        hotel.book_room(2)
        hotel.book_room(3)
        hotel.book_room(4)
        hotel.book_room(5)

        self.assertEqual(0, hotel.capacity)

    def test_book_room_raisesRoomNumberNotValid_whenRoomNumIsNotValid(self):

        with self.assertRaises(RoomNumberNotValid):
            self.hotel.book_room(6)

    def test_book_room_raisesRoomNumberNotValid_whenRoomNIsNotAvailabe(self):
        self.hotel.book_room(1)

        with self.assertRaises(RoomAlreadyBooked):
            self.hotel.book_room(1)

    def test_book_room_booksARoom(self):
        self.hotel.book_room(1)

        self.assertEqual(1, self.hotel.get_room_status(1))
        self.assertEqual(4, self.hotel.capacity)



