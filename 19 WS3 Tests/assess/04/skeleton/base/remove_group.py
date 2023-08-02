from base.base_command import BaseCommand

class RemoveGroup(BaseCommand):
    def execute(self):
        test_group_id = int(self._params[0])
        test_group = self._app_data.find_test_group_by_id(test_group_id)

        if test_group:
            self._app_data.remove_test_group(test_group_id)  # Remove the TestGroup and its tests

            return f"Group #{test_group_id} removed"

        return f"Group with id #{test_group_id} not found"