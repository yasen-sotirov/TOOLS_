from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class RemoveGroupByIdCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_group_id = int(self._params[0])
        self._app_data.remove_test_group_by_id(test_group_id)

        return f'Group #{test_group_id} removed'
