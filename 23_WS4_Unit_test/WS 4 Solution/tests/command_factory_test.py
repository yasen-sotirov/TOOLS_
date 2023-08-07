import unittest
from commands.add_test import AddTestCommand
from commands.add_test_group import AddTestGroupCommand
from commands.add_test_run import AddTestRunCommand
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand
from commands.view_group import ViewGroupCommand
from commands.view_system import ViewSystemCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class Create_Should(unittest.TestCase):
    def test_raiseError_invalidCommandName(self):
        # Arrange
        input_line = 'asd 1 2 3'
        cmd_factory, app_data = test_setup()

        # Act & Assert
        with self.assertRaises(ApplicationError):
            command = cmd_factory.create(input_line)

    def test_createAddTestCommand_withCorrectParams(self):
        # Arrange
        input_line = 'addtest 1 description'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, AddTestCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1', 'description'), command.params)

    def test_createAddTestGroupCommand_withCorrectParams(self):
        # Arrange
        input_line = 'addtestgroup group_name'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, AddTestGroupCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('group_name',), command.params)

    def test_createAddTestRunCommand_withCorrectParams(self):
        # Arrange
        input_line = 'addtestrun 1 pass 5'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, AddTestRunCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1', 'pass', '5'), command.params)

    def test_createRemoveGroupCommand_withCorrectParams(self):
        # Arrange
        input_line = 'removegroup 1'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, RemoveGroupCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1',), command.params)

    def test_createTestReportCommand_withCorrectParams(self):
        # Arrange
        input_line = 'testreport 2'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, TestReportCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('2',), command.params)

    def test_createViewGroupCommand_withCorrectParams(self):
        # Arrange
        input_line = 'viewgroup 3'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, ViewGroupCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('3',), command.params)

    def test_createViewSystemCommand_withCorrectParams(self):
        # Arrange
        input_line = 'viewsystem'
        cmd_factory, app_data = test_setup()

        # Act
        command = cmd_factory.create(input_line)

        # Assert
        self.assertIsInstance(command, ViewSystemCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(tuple(), command.params)
