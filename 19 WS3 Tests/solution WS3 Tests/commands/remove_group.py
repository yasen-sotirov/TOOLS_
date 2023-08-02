from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class RemoveGroupCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        group_id = int(self.params[0])

        if self.app_data.remove_group(group_id):
            return f'Group #{group_id} removed'
        else:
            return f'Group #{group_id} not found'
