from commands.base.base_command import BaseCommand
from models.constants.test_result import TestResult
from models.test_run import TestRun

class AddTestRun(BaseCommand):
    def execute(self):
        test_id = int(self.params[0])
        result = self.params[1].lower()
        runtime_ms = int(self.params[2])

        test = self.app_data.find_test_by_id(test_id)
        if test is None:
            raise ValueError(f"Test with id {test_id} not found")

        if result not in [TestResult.PASS, TestResult.FAIL]:
            raise ValueError("Invalid test result value. The result must be 'pass' or 'fail'.")

        new_test_run = TestRun(result, runtime_ms)
        test.add_test_run(new_test_run)

        return f'TestRun registered'
