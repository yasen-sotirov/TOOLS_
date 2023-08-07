import unittest
from errors.application_error import ApplicationError

from models.test import Test
from models.test_run import TestRun
from models.constants.test_result import TestResult

VALID_ID = 1
VALID_DESC = 'a_desc'


class Initializer_Should(unittest.TestCase):
    def test_assignValues(self):
        # Arrange & Act
        test = Test(VALID_ID, VALID_DESC)

        # Assert
        self.assertEqual(VALID_ID, test.id)
        self.assertEqual(VALID_DESC, test.description)
        self.assertEqual((), test.test_runs)

    def test_raiseError_invalidDescription(self):
        # Arrange, Act & Assert
        with self.assertRaises(ApplicationError):
            test = Test(VALID_ID, '')


class AddTestRun_Should(unittest.TestCase):
    def test_addTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        tr2 = TestRun(TestResult.FAIL, 5)

        # Act
        test.add_test_run(tr1)
        test.add_test_run(tr2)
        test.add_test_run(tr1)

        # Assert
        self.assertEqual((tr1, tr2, tr1), test.test_runs)


class PassingTestRuns_Should(unittest.TestCase):
    def test_returnCorrectRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        tr2 = TestRun(TestResult.FAIL, 5)
        test.add_test_run(tr1)
        test.add_test_run(tr2)
        test.add_test_run(tr1)

        # Act & Assert
        self.assertEqual((tr1, tr1), test.passing_test_runs)

    def test_returnEmpty_whenNoPassingTests(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr2 = TestRun(TestResult.FAIL, 5)
        test.add_test_run(tr2)
        test.add_test_run(tr2)

        # Act & Assert
        self.assertEqual((), test.passing_test_runs)


class FailedTestRuns_Should(unittest.TestCase):
    def test_returnCorrectRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        tr2 = TestRun(TestResult.FAIL, 5)
        test.add_test_run(tr1)
        test.add_test_run(tr2)
        test.add_test_run(tr1)

        # Act & Assert
        self.assertEqual((tr2,), test.failed_test_runs)

    def test_returnEmpty_whenNoFailedTests(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        test.add_test_run(tr1)
        test.add_test_run(tr1)

        # Act & Assert
        self.assertEqual((), test.failed_test_runs)


class TotalRuntime_Should(unittest.TestCase):
    def test_returnCorrectValue(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        tr2 = TestRun(TestResult.PASS, 4)
        tr3 = TestRun(TestResult.PASS, 8)
        tr4 = TestRun(TestResult.FAIL, 9)
        test.add_test_run(tr1)
        test.add_test_run(tr2)
        test.add_test_run(tr1)  # add tr1 second time
        test.add_test_run(tr3)
        test.add_test_run(tr4)

        # Act & Assert
        self.assertEqual(5 + 4 + 5 + 8 + 9, test.total_runtime)

    def test_returnZero_whenNoTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)

        # Act & Assert
        self.assertEqual(0, test.total_runtime)


class AvgRuntime_Should(unittest.TestCase):
    def test_returnCorrectValue(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        tr1 = TestRun(TestResult.PASS, 5)
        tr2 = TestRun(TestResult.PASS, 4)
        tr3 = TestRun(TestResult.PASS, 8)
        tr4 = TestRun(TestResult.FAIL, 9)
        test.add_test_run(tr1)
        test.add_test_run(tr2)
        test.add_test_run(tr1)  # add tr1 second time
        test.add_test_run(tr3)
        test.add_test_run(tr4)

        # Act & Assert
        self.assertAlmostEqual((5 + 4 + 5 + 8 + 9) / 5, test.avg_runtime)

    def test_returnZero_whenNoTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)

        # Act & Assert
        self.assertAlmostEqual(0.0, test.avg_runtime)


class Str_Should(unittest.TestCase):
    def test_formatCorrectly(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        expected = f'#{VALID_ID}. [{VALID_DESC}]: 0 runs'

        # Act
        actual = f'{test}'

        # Assert
        self.assertEqual(expected, actual)

    def test_formatCorrectly_withTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        test.add_test_run(TestRun(TestResult.PASS, 2))
        expected = f'#{VALID_ID}. [{VALID_DESC}]: 1 runs'

        # Act
        actual = f'{test}'

        # Assert
        self.assertEqual(expected, actual)


class GenerateReport_Should(unittest.TestCase):
    def test_formatCorrectly_withTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        test.add_test_run(TestRun(TestResult.PASS, 3))
        test.add_test_run(TestRun(TestResult.FAIL, 4))
        expected = '\n'.join([
            f'#{VALID_ID}. [{VALID_DESC}]: 2 runs',
            '- Passing: 1',
            '- Failing: 1',
            '- Total runtime: 7ms',
            '- Average runtime: 3.5ms'
        ])

        # Act
        actual = test.generate_report()

        # Assert
        self.assertEqual(expected, actual)

    def test_formatCorrectly_noTestRuns(self):
        # Arrange
        test = Test(VALID_ID, VALID_DESC)
        expected = f'#{VALID_ID}. [{VALID_DESC}]: 0 runs'

        # Act
        actual = test.generate_report()

        # Assert
        self.assertEqual(expected, actual)
