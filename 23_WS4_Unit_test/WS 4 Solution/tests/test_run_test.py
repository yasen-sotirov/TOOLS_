import unittest
from errors.application_error import ApplicationError

from models.test_run import TestRun
from models.constants.test_result import TestResult


class Initializer_Should(unittest.TestCase):
    def test_assignValues(self):
        # Arrange
        runtime_ms = 1
        test_result = TestResult.PASS

        # Act
        test_run = TestRun(test_result, runtime_ms)

        # Assert
        self.assertEqual(test_result, test_run.test_result)
        self.assertEqual(runtime_ms, test_run.runtime_ms)

    def test_raiseError_invalidZeroRuntime(self):
        # Arrange, Act & Assert
        with self.assertRaises(ApplicationError):
            test_run = TestRun(TestResult.FAIL, 0)

    def test_raiseError_negativeRuntime(self):
        # Arrange, Act & Assert
        with self.assertRaises(ApplicationError):
            test_run = TestRun(TestResult.FAIL, -1)
