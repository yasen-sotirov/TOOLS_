import unittest

from custom_exceptions import RoomNumberNotValid, RoomAlreadyBooked
from hotel import Hotel


class Hotel_Should(unittest.TestCase):


    def test_initializerSetsAttributes(self):
        #Arrange
        name = "Seaside"
        rooms_count = 5

        #Act
        hotel = Hotel(name, rooms_count)

        #Assert
        self.assertEqual(name, hotel.name)
        self.assertEqual(5, hotel.room_count)
        self.assertIsInstance(hotel, Hotel)

    def test_nameIsReadonly(self):
        # Arrange
        hotel = Hotel("Seaside", 5)

        # Act & Assert
        with self.assertRaises(AttributeError):
            hotel.name = "Bla"

    def test_capacity_returnsCorrectValue(self):
        # Arrange
        hotel = Hotel("Seaside", 5)

        # Act & Assert
        self.assertEqual(5, hotel.capacity)

    def test_capacity_returnsCorrectValue_whenRoomsAreAvailable(self):
        # Arrange
        hotel = Hotel("Seaside", 5)
        hotel.book_room(1)

        # Act & Assert
        self.assertEqual(4, hotel.capacity)

    def test_capacity_returnsCorrectValue_whenAllRoomsAreNotAvailable(self):
        # Arrange
        hotel = Hotel("Seaside", 5)
        hotel.book_room(1)
        hotel.book_room(2)
        hotel.book_room(3)
        hotel.book_room(4)
        hotel.book_room(5)

        # Act & Assert
        self.assertEqual(0, hotel.capacity)

    def test_book_room_raisesRoomNumberNotValid_whenRoomNumIsNotValid(self):
        # Arrange
        hotel = Hotel("Seaside", 5)

        # Act & Assert
        with self.assertRaises(RoomNumberNotValid):
            hotel.book_room(6)

    def test_book_room_raisesRoomNumberNotValid_whenRoomNIsNotAvailabe(self):
        # Arrange
        hotel = Hotel("Seaside", 5)
        hotel.book_room(1)

        # Act & Assert
        with self.assertRaises(RoomAlreadyBooked):
            hotel.book_room(1)

    def test_book_room_booksARoom(self):
        # Arrange
        hotel = Hotel("Seaside", 5)

        # Act
        hotel.book_room(1)

        # Assert
        self.assertEqual(1, hotel.get_room_status(1))
        self.assertEqual(4, hotel.capacity)



