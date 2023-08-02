from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewGroupCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_group_id = int(self._params[0])
        test_group = self._app_data.find_test_group_by_id(test_group_id)
        result = f'#{test_group.id}. {test_group.name} ({len(test_group.tests)} tests)'
        for test in test_group.tests:
            result += f'\n  #{test.id}. [{test.description}]: {len(test.test_runs)} runs'
        return result
