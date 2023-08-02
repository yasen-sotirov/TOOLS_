from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData



class ViewGroupCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        group_id = int(self.params[0])
        group = self.app_data.find_group(group_id)
        if group is None:
            return f'Group #{group_id} not found'
        else:
            return group.view()