from base.base_command import BaseCommand
from models.test import Test

class AddTest(BaseCommand):
    def execute(self):
        test_group_id, description = int(self._params[0]), self._params[1]
        test_group = self._app_data.find_test_group_by_id(test_group_id)

        if test_group:
            test_id = len(test_group.tests) + 1  # Get the next available TestId
            test = Test(test_id, description)
            test_group.add_test(test)  # Add the created Test to the TestGroup

            return f"Test #{test_id} added to group #{test_group_id}"

        return f"Group with id #{test_group_id} not found"