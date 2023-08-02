from base.base_command import BaseCommand
from models.test_group import TestGroup

class AddTestGroup(BaseCommand):
    def execute(self):
        name = self._params[0]
        test_group_id = len(self._app_data.groups) + 1  # Get the next available TestGroupId

        test_group = TestGroup(test_group_id, name)
        self._app_data.add_test_group(test_group)  # Add the created TestGroup to the ApplicationData

        return f"Group #{test_group_id} created"