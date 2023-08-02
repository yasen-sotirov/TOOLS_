from core.application_data import ApplicationData
from commands.add_test_group_command import AddTestGroupCommand
from commands.add_test_command import AddTestCommand
from commands.add_test_run_command import AddTestRunCommand
from commands.remove_group_by_id_command import RemoveGroupByIdCommand
from commands.test_report_command import TestReportCommand
from commands.view_group_command import ViewGroupCommand
from commands.view_system_command import ViewSystemCommand


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):

        cmd, *params = input_line.split()

        if cmd.lower() == 'addtestgroup':
            return AddTestGroupCommand(params, self._app_data)
        if cmd.lower() == 'addtest':
            return AddTestCommand(params, self._app_data)
        if cmd.lower() == 'addtestrun':
            return AddTestRunCommand(params, self._app_data)
        if cmd.lower() == 'removegroup':
            return RemoveGroupByIdCommand(params, self._app_data)
        if cmd.lower() == 'testreport':
            return TestReportCommand(params, self._app_data)
        if cmd.lower() == 'viewgroup':
            return ViewGroupCommand(params, self._app_data)
        if cmd.lower() == 'viewsystem':
            return ViewSystemCommand(params, self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
