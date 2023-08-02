from commands.base.base_command import BaseCommand
from models.constants.test_result import TestResult

class TestReport(BaseCommand):
    def execute(self):
        test_id = int(self.params[0])

        test = self.app_data.find_test_by_id(test_id)
        if test is None:
            raise ValueError(f"Test with id {test_id} not found.")

        passing_runs = 0
        failing_runs = 0
        total_runtime = 0

        for test_run in test.test_runs:
            if test_run.test_result == TestResult.PASS:
                passing_runs += 1
            elif test_run.test_result == TestResult.FAIL:
                failing_runs += 1
            total_runtime += test_run.runtime_ms

        if len(test.test_runs) > 0:
            avg_runtime = total_runtime / len(test.test_runs)
        else:
            avg_runtime = 0

        report = f"#{test.id}. [{test.description}]: {len(test.test_runs)} runs\n"
        report += f"- Passing: {passing_runs}\n"
        report += f"- Failing: {failing_runs}\n"
        report += f"- Total runtime: {total_runtime}ms\n"
        report += f"- Average runtime: {avg_runtime:.1f}ms"

        return report
