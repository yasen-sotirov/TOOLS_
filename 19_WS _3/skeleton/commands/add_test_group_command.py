from commands.base.base_command import BaseCommand


class AddTestGroupCommand(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        test_group_name = self._params[0]
        self._app_data.create_test_group(test_group_name)

        return f'The group {test_group_name} was created'
