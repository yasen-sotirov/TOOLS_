from unittest import TestCase
from errors.application_error import ApplicationError
from models.test_run import TestRun
from models.constants.test_result import TestResult


class Test_run_should(TestCase):

    def test_initializer_sets_attributes_correctly(self):
        # Arrange
        test_result = TestResult
        runtime_ms = 5

        # Act
        test_run_1 = TestRun(test_result, runtime_ms)

        # Assert
        self.assertEquals(test_result, test_run_1.test_result)
        self.assertEquals(runtime_ms, test_run_1.runtime_ms)


    def test_constructor_raise_error_when_attributes_is_not_correct(self):
        with self.assertRaises(ApplicationError):
            _ = TestRun("bla", - 1)


    def test_invalid_runtime_ms(self):
        # Проверяваме дали създаването на обект с неположително (или нулево) време на изпълнение дава грешка
        # Arrange & Act

        test_result = TestResult("fail")
        runtime_ms = 0
        with self.assertRaises(ApplicationError):
            test_run = TestRun(test_result, runtime_ms)




    def test_valid_runtime_ms(self):
        # Проверяваме дали създаването на обект с положително време на изпълнение работи коректно
        test_result = TestResult("pass")
        runtime_ms = 100
        test_run = TestRun(test_result, runtime_ms)
        self.assertEqual(test_run._runtime_ms, runtime_ms)









