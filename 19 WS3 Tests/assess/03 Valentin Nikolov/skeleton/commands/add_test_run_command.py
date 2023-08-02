from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test_run import TestRun


class AddTestRunCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_id, result, runtime = self._params
        test_id = int(test_id)
        runtime = int(runtime)
        test = self._app_data.find_test_by_id(test_id)
        test_run = TestRun(result, runtime)
        test._test_runs.append(test_run)

        return 'TestRun registered'
