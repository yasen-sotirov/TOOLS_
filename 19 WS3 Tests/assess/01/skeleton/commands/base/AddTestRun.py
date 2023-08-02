from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test_run import TestRun
from models.test import Test
from models.test_group import TestGroup






class AddTestRun(BaseCommand):

    current_id = 0
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params,app_data)

        self._params = params
        AddTestRun.current_id += 1
        self._id = AddTestRun.current_id
        
        self._app_data = app_data



    def execute(self):


        Test_id = int(self._params[0])

        result = self._params[1]

        runTime = self._params[2]


        test = self.app_data.find_test_by_id(Test_id)
        
        test_run = TestRun(result,runTime)

        test.add_test_run(test_run)

        self.app_data._test_groups.append(test._test_runs)
        



        return 'TestRun registered'
        
