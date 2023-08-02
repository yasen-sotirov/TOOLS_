from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class TestReportCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_id = int(self._params[0])
        test = self._app_data.find_test_by_id(test_id)
        test_runs_count = len(test.test_runs)

        passing_runs_count = 0
        failing_runs_count = 0
        total_runtime = 0

        for run in test.test_runs:
            if run.test_result == 'pass':
                passing_runs_count += 1
            else:
                failing_runs_count += 1
            total_runtime += run.runtime_ms

        avg_runtime = total_runtime/test_runs_count

        return f'''#{test.id}. [{test.description}]: {test_runs_count} runs
- Passing: {passing_runs_count}
- Failing: {failing_runs_count}
- Total runtime: {total_runtime}ms
- Average runtime: {avg_runtime:.1f}ms'''
