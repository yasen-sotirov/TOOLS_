from commands.base.base_command import BaseCommand
from models.test_group import TestGroup

class AddTestGroup(BaseCommand):
    def execute(self):
        group_name = self._params[0]
        group_id = len(self.app_data.groups) + 1
        test_group = TestGroup(group_id, group_name)
        self.app_data._test_groups.append(test_group)
        return f'Group #{group_id} created'