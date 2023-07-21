from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewSystemCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        if len(self.app_data.groups) == 0:
            return 'No test groups in the system'
        else:
            return '\n'.join(
                [f'Test Reporter System ({len(self.app_data.groups)} test groups)'] +
                [f'  {group}' for group in self.app_data.groups])
