from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test import Test



class Add_Test(BaseCommand):

    current_id = 0
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params,app_data)

        self._params = params
        Add_Test.current_id += 1
        self._id = Add_Test.current_id
        
        self._app_data = app_data



    def execute(self):


        Test_group_id = int(self._params[0])

        description = self._params[1]

        test_group = self.app_data.find_group_by_id(Test_group_id)

        test = Test(self._id,description)

        test_group.add_test(test)

        self.app_data._test_groups.append(test_group._tests)

        return f'Test #{self._id} added to group #{Test_group_id}'
        

        