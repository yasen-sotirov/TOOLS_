from commands.base.base_command import BaseCommand
from models.test_group import TestGroup
from core.application_data import ApplicationData


class AddTestGroup(BaseCommand):

    current_id = 0
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(params,app_data)

        self._params = params
        AddTestGroup.current_id += 1
        self._id = AddTestGroup.current_id
        
        self._app_data = app_data



    def execute(self):

        name = self._params[0]

        self._app_data.create_testGroup(self._id,name)

        return f'Group #{self._id} created'
        




