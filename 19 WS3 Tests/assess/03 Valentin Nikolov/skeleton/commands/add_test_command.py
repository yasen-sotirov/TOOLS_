from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test import Test


class AddTestCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_group_id, description = self._params
        test_group_id = int(test_group_id)
        test_group = self._app_data.find_test_group_by_id(test_group_id)
        self._app_data.tests_id_tracker += 1
        test = Test(self._app_data.tests_id_tracker, description)
        test_group._tests.append(test)

        return f'Test #{test.id} added to group #{test_group.id}'
