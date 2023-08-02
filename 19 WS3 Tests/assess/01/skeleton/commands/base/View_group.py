from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.test_run import TestRun
from models.test import Test
from models.test_group import TestGroup






class View_group(BaseCommand):


    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params,app_data)

        self._params = params

        self._app_data = app_data



    def execute(self):


        testgroup_id = int(self._params[0])

        return self.app_data.view_group(testgroup_id)

        