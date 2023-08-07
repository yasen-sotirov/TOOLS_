import unittest
from errors.application_error import ApplicationError
from models.test import Test

from models.test_group import TestGroup

VALID_ID = 1
VALID_NAME = 'a_name'


class Initializer_Should(unittest.TestCase):
    def test_assignValues(self):
        # Arrange & Act
        test_group = TestGroup(VALID_ID, VALID_NAME)

        # Assert
        self.assertEqual(VALID_ID, test_group.id)
        self.assertEqual(VALID_NAME, test_group.name)
        self.assertEqual(tuple(), test_group.tests)

    def test_raiseError_invalidName(self):
        # Arrange, Act & Assert
        with self.assertRaises(ApplicationError):
            TestGroup(VALID_ID, '')


class AddTest_Should(unittest.TestCase):
    def test_addTest_whenNotPreviouslyAdded(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        test = Test(VALID_ID, VALID_NAME)

        # Act
        test_group.add_test(test)

        # Assert
        self.assertEqual(tuple([test]), test_group.tests)

    def test_doNothing_whenAlreadyAdded(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        test = Test(VALID_ID, VALID_NAME)
        test_group.add_test(test)

        # Act
        test_group.add_test(test)

        # Assert
        self.assertEqual(1, len(test_group.tests))

    def test_addMoreThanOne_whenTestsAreDifferent(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        test1 = Test(VALID_ID, VALID_NAME)
        test2 = Test(VALID_ID + 1, VALID_NAME)
        test_group.add_test(test1)

        # Act
        test_group.add_test(test2)

        # Assert
        self.assertEqual(2, len(test_group.tests))


class Str_Should(unittest.TestCase):
    def test_returnCorrectFormat_zeroTests(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        expected = f'#{VALID_ID}. {VALID_NAME} (0 tests)'

        # Act
        actual = f'{test_group}'

        # Assert
        self.assertEqual(expected, actual)

    def test_returnCorrectFormat_severalTests(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        test_group.add_test(Test(VALID_ID, VALID_NAME))
        test_group.add_test(Test(VALID_ID + 1, VALID_NAME))
        expected = f'#{VALID_ID}. {VALID_NAME} (2 tests)'

        # Act
        actual = f'{test_group}'

        # Assert
        self.assertEqual(expected, actual)


class View_Should(unittest.TestCase):
    def test_returnCorrectFormat_severalTests(self):
        # Arrange
        test1_id = 2
        test1_desc = 'test1_desc'
        test2_id = 5
        test2_desc = 'test2_desc'
        test_group = TestGroup(VALID_ID, VALID_NAME)
        test_group.add_test(Test(test1_id, test1_desc))
        test_group.add_test(Test(test2_id, test2_desc))
        expected = '\n'.join([
            f'#{VALID_ID}. {VALID_NAME} (2 tests)',
            f'  #{test1_id}. [{test1_desc}]: 0 runs',
            f'  #{test2_id}. [{test2_desc}]: 0 runs',
        ])

        # Act
        actual = test_group.view()

        # Assert
        self.assertEqual(expected, actual)

    def test_returnCorrectFormat_zeroTests(self):
        # Arrange
        test_group = TestGroup(VALID_ID, VALID_NAME)
        expected = f'#{VALID_ID}. {VALID_NAME} (0 tests)'

        # Act
        actual = test_group.view()

        # Assert
        self.assertEqual(expected, actual)
