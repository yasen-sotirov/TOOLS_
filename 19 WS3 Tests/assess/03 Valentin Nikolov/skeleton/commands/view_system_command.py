from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewSystemCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        result = f'Test Reporter System ({len(self._app_data.groups)} test groups)'
        for test_group in self._app_data.groups:
            result += f'\n  #{test_group.id}. {test_group.name} ({len(test_group.tests)} tests)'

        return result
