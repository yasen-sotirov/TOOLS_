from commands.base.base_command import BaseCommand
from models.test_group import TestGroup

class RemoveGroup(BaseCommand):
    def execute(self):
        test_group_id = int(self.params[0])

        test_group = self.app_data.find_test_group_by_id(test_group_id)
        if test_group is None:
            raise ValueError(f"TestGroup with id {test_group_id} not found.")

        self.app_data.remove_test_group(test_group)

        return f"Group #{test_group_id} removed"

