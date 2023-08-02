from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData



class TestReportCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        test_id = int(self.params[0])
        test = self.app_data.find_test(test_id)
        if test is None:
            return f'Test #{test_id} not found'
        else:
            return test.generate_report()
        