# from base_command import BaseCommand
# from models.test import Test
# from models.test_group import TestGroup

# class AddTest(BaseCommand):
#     def execute(self):
#         test_description = self._params[0]
#         test_group_id = self._params[1]
#         test = Test(test_group_id, test_description)
        
        
from commands.base.base_command import BaseCommand
from models.test import Test

class AddTest(BaseCommand):
    def execute(self):
        test_group_id = int(self.params[0])
        description = " ".join(self.params[1:]) 

        test_group = self.app_data.find_test_group_by_id(test_group_id)
        if test_group is None:
            raise ValueError(f"TestGroup with id {test_group_id} not found.")

        test_id = self.app_data.generate_next_test_id(test_group_id)

        new_test = Test(test_id, description)
        test_group.add_test(new_test)

        return f"Test #{test_id} added to group #{test_group.id}"

