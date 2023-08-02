from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test_group import TestGroup


class AddTestGroupCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name = self._params[0]
        self._app_data.groups_id_tracker += 1
        test_group = TestGroup(self._app_data.groups_id_tracker, name)
        self._app_data.add_test_group(test_group)

        return f'Group #{test_group.id} created'
