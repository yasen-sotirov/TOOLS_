from commands.base.base_command import BaseCommand
from models.test import Test


class AddTestCommand(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        test_name = int(self._params[0])
        description = self._params[1]

        new_test = Test(test_name, description)

        return new_test





