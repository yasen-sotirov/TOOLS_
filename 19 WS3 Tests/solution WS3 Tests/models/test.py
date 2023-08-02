from models.constants.test_result import TestResult
from models.test_run import TestRun


class Test:
    def __init__(self, id: int, description: str):
        self._id = id
        self._description = description
        self._test_runs: list[TestRun] = []

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    def add_test_run(self, test_run: TestRun):
        self._test_runs.append(test_run)

    def generate_report(self):
        total_runs = len(self.test_runs)
        passing_count = len(
            [t for t in self.test_runs if t.test_result == TestResult.PASS])
        failing_count = total_runs - passing_count
        total_runtime = sum(t.runtime_ms for t in self.test_runs)
        average_runtime = (total_runtime / total_runs) if total_runs > 0 else 0.0

        return '\n'.join([
            f'{self}',
            f'- Passing: {passing_count}',
            f'- Failing: {failing_count}',
            f'- Total runtime: {total_runtime}ms',
            f'- Average runtime: {average_runtime:.1f}ms'
        ])

    def __str__(self):
        return f'#{self.id}. [{self.description}]: {len(self.test_runs)} runs'
