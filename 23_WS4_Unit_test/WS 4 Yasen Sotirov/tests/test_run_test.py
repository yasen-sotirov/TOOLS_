from unittest import TestCase
from errors.application_error import ApplicationError
from models.test_run import TestRun
from models.constants.test_result import TestResult


class Test_run_should(TestCase):

    def test_initializerSetsAttributesCorrectly(self):
        # Arrange
        test_result = TestResult
        runtime_ms = 5

        # Act
        test_run_1 = TestRun(test_result, runtime_ms)

        # Assert
        self.assertEquals(test_result, test_run_1.test_result)
        self.assertEquals(runtime_ms, test_run_1.runtime_ms)


    def test_initializerRaiseErrorWhenAttributesIsNotCorrect(self):
        # Arrange
        test_result = TestResult
        runtime_ms = - 1

        # Act
        test_run_1 = TestRun(test_result, runtime_ms)

        # Assert
        with self.assertRaises(ApplicationError):
            test_run_1.runtime_ms = 6

        