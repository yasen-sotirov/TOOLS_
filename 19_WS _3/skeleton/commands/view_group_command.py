from core.application_data import ApplicationData
from commands.base.base_command import BaseCommand


class ViewGroupCommand(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        # задава името
        test_name = self._params[0]

        self._app_data.create_test_group(test_name)

        return f'The group {test_name} was created'
