from core.application_data import ApplicationData
from commands.add_test_group_command import AddTestGroupCommand
from commands.add_test_command import AddTestCommand
from commands.add_test_run_command import AddTestRunCommand
from commands.test_report_command import TestReportCommand
from commands.remove_group_command import RemoveGroupCommand
from commands.view_group_command import ViewGroupCommand
from commands.view_system_command import ViewSystemCommand

# получава входа
# определя коя команда е поискана
# създава и връща правилната команда


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create_command(self, input_line):
        # разделя импута на команди и параметри
        cmd, *params = input_line.split()

        if cmd == "AddTestGroup".lower():       # връща от папката с командите
            return AddTestGroupCommand(params, self._app_data)

        if cmd == "AddTest".lower():
            return AddTestCommand(params, self._app_data)

        if cmd == "AddTestRun".lower():
            return AddTestRunCommand(params, self._app_data)

        if cmd == "TestReport".lower():
            return TestReportCommand(params, self._app_data)

        if cmd == "RemoveGroup".lower():
            return RemoveGroupCommand(params, self._app_data)

        if cmd == "ViewGroup".lower():
            return ViewGroupCommand(params, self._app_data)

        if cmd == "ViewSystem.lower()":
            return ViewSystemCommand(params, self._app_data)

        raise ValueError(f'Invalid command!')

