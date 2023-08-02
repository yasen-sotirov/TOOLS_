from base.base_command import BaseCommand
from models.constants.test_result import TestResult
from models.test_run import TestRun

class AddTestRun(BaseCommand):
    def execute(self):
        test_id, result, runtime = int(self._params[0]), self._params[1], int(self._params[2])
        test = self._app_data.find_test_by_id(test_id)

        if test:
            if result in [TestResult.PASS, TestResult.FAIL]:
                test_run = TestRun(result, runtime)
                test.add_test_run(test_run)  # Add the created TestRun to the Test

                return "TestRun registered"

            return f"Invalid test result: {result}. It should be 'pass' or 'fail'"
        
        return f"Test with id #{test_id} not found"