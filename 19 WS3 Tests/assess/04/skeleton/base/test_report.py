from base.base_command import BaseCommand

class TestReport(BaseCommand):
    def execute(self):
        test_id = int(self._params[0])
        test = self._app_data.find_test_by_id(test_id)

        if test:
            test_description = test.description
            test_runs = test.test_runs
            test_runs_count = len(test_runs)
            passing_runs_count = sum(1 for run in test_runs if run.test_result == "pass")
            failing_runs_count = test_runs_count - passing_runs_count
            total_runtime = sum(run.runtime_ms for run in test_runs)
            avg_runtime = total_runtime / test_runs_count if test_runs_count > 0 else 0.0

            test_report = (
                f"#{test_id}. [{test_description}]: {test_runs_count} runs\n"
                f"- Passing: {passing_runs_count}\n"
                f"- Failing: {failing_runs_count}\n"
                f"- Total runtime: {total_runtime}ms\n"
                f"- Average runtime: {avg_runtime:.1f}ms"
            )
            return test_report

        return f"Test with id #{test_id} not found"