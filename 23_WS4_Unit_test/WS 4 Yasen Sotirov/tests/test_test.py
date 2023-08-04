from unittest import TestCase
from models.test import Test
from errors.application_error import ApplicationError
from models.test_run import TestRun
from models.constants.test_result import TestResult

VALID_ID = 1
VALID_DESCRIPTION = "description"
VALID_TEST = Test(VALID_ID, VALID_DESCRIPTION)

VALID_TEST.add_test_run(TestRun(TestResult.PASS, 1))
VALID_TEST.add_test_run(TestRun(TestResult.PASS, 2))

VALID_TEST.add_test_run(TestRun(TestResult.FAIL, 3))
VALID_TEST.add_test_run(TestRun(TestResult.FAIL, 4))

class Test_Should(TestCase):

    def test_Constructor_assign_value_correctly(self):
        self.assertEqual(VALID_ID, VALID_TEST.id)
        self.assertEqual(VALID_DESCRIPTION, VALID_TEST.description)

    def test_Constructor_raise_error_when_description_isNone(self):
        with self.assertRaises(ApplicationError):
            _ = Test(VALID_ID, None)

    def test_PassingTestRun_return_only_passing_test_runs(self):
        self.assertEqual(2, len(VALID_TEST.passing_test_runs))

    def test_FailedTestRuns_return_only_failed_test_runs(self):
        self.assertEqual(2, len(VALID_TEST.failed_test_runs))

    def test_TotalRunTime_return_correct_time(self):
        self.assertEqual(10, VALID_TEST.total_runtime)

    def test_averageRubTime_return_correct_time(self):
        self.assertEqual(2.5, VALID_TEST.avg_runtime)

    def test_addTestRun_add_sameTestRun_correctly(self):
        test_run_same = TestRun("fail", 100)
        VALID_TEST.add_test_run(test_run_same)
        self.assertEqual(5, len(VALID_TEST.test_runs))

    def test_addTestRun_add_otherTestRuns_correctly(self):
        test_run_other = TestRun("pass", 100)
        VALID_TEST.add_test_run(test_run_other)
        self.assertEqual(5, len(VALID_TEST.test_runs))

    def test_generateReport_work_correctly_when_there_are_test_runs(self):
        expected_report = '\n'.join([
            f'{VALID_TEST}',
            f'- Passing: {len(VALID_TEST.passing_test_runs)}',
            f'- Failing: {len(VALID_TEST.failed_test_runs)}',
            f'- Total runtime: {VALID_TEST.total_runtime}ms',
            f'- Average runtime: {VALID_TEST.avg_runtime:.1f}ms'
        ])
        self.assertEqual(expected_report, VALID_TEST.generate_report())

    def test_generateReport_work_correctly_when_there_are_not_test_runs(self):
        test_no_runs = Test(2, "empty")
        expected_output = f'#{test_no_runs.id}. [{test_no_runs.description}]: {len(test_no_runs.test_runs)} runs'
        self.assertEqual(expected_output, test_no_runs.generate_report())

    def test_correct_str_representation(self):
        expected_output = f'#1. [description]: 4 runs'
        self.assertEqual(expected_output, VALID_TEST.__str__())



