import unittest
from unittest.mock import Mock
from commands.show_category import ShowCategoryCommand
from errors.invalid_params import InvalidParams


class ShowCategoryCommand_Should(unittest.TestCase):
    def test_constructor_createsSuccessfully(self):
        try:
            # Arrange, Act, Assert
            _ = ShowCategoryCommand(['cat'], Mock())

            # nothing to assert
        except:
            self.fail('ShowCategoryCommand failed with valid data')

    def test_constructor_raisesError_params_tooFew(self):
        # Arrange, Act, Assert
        with self.assertRaises(InvalidParams):
            ShowCategoryCommand([], Mock())

    def test_constructor_raisesError_params_tooMuch(self):
        # Arrange, Act, Assert
        with self.assertRaises(InvalidParams):
            ShowCategoryCommand(['cat1', 'cat2'], Mock())

    def test_execute_returnsOutput(self):
        # Arrange
        FAKE_CATEGORY_OUTPUT = 'fake output'
        CMD_NAME = 'cmd_name'
        category = Mock()
        category.to_string = lambda: FAKE_CATEGORY_OUTPUT

        app_data = Mock()
        app_data.find_category_by_name = lambda name: category if name == CMD_NAME else None

        command = ShowCategoryCommand([CMD_NAME], app_data)

        # Act
        actual_output = command.execute()

        # Assert
        self.assertEqual(FAKE_CATEGORY_OUTPUT, actual_output)
