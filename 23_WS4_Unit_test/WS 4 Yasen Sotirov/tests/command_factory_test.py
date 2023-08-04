from unittest import TestCase
from core.command_factory import CommandFactory
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory

from commands.add_test_group import AddTestGroupCommand
from commands.add_test_run import AddTestRunCommand
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand
from commands.view_group import ViewGroupCommand
from commands.view_system import ViewSystemCommand
from commands.add_test import AddTestCommand


app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
models_factory = ModelsFactory()

class Command_factory_should(TestCase):

    def test_command_exists_for_addtest_command(self):
        input_line = "AddTesT 1 test_name"
        command = cmd_factory.create(input_line)
        expected_output = AddTestCommand([1, "test_name"], app_data, models_factory)

        self.assertEqual(expected_output, command)