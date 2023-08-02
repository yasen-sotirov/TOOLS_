
from commands.base.add_test_group import AddTestGroup
from core.application_data import ApplicationData
from commands.base.add_test import AddTest
from commands.base.add_test_run import AddTestRun
from commands.base.remove_group import RemoveGroup
from commands.base.test_report import TestReport
from commands.base.view_group import ViewGroup
from commands.base.view_system import ViewSystem



class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        input_parts = input_line.split()
        command_name = input_parts[0].lower()

        if command_name == "addtestgroup":
            return AddTestGroup(input_parts[1:], self._app_data)
        
        elif command_name == "addtest":
            return AddTest(input_parts[1:], self._app_data)
        
        elif command_name == "addtestrun":
            return AddTestRun(input_parts[1:], self._app_data)
        
        elif command_name == "removegroup":
            return RemoveGroup(input_parts[1:], self._app_data)
        
        elif command_name == "testreport":
            return TestReport(input_parts[1:], self._app_data)
        
        elif command_name == "viewgroup":
            return ViewGroup(input_parts[1:], self._app_data)
        
        elif command_name == "viewsystem":
            return ViewSystem(input_parts[1:], self._app_data)

        else:
            raise ValueError(f"Invalid command: {command_name}")
