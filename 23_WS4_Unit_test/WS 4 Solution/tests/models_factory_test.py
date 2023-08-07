from unittest import TestCase

from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test import Test
from models.test_group import TestGroup
from models.test_run import TestRun


class CreateTest_Should(TestCase):
    def test_createValidTestInstance(self):
        # Arrange
        desc = 'test description'
        models_factory = ModelsFactory()

        # Act
        test = models_factory.create_test(desc)

        # Assert
        self.assertIsInstance(test, Test)
        self.assertEqual(1, test.id)
        self.assertEqual(desc, test.description)
        self.assertEqual((), test.test_runs)

    def test_createTestsWithConsecutiveIds(self):
        # Arrange
        desc = 'test description'
        models_factory = ModelsFactory()

        # Act
        test_1 = models_factory.create_test(desc)
        test_2 = models_factory.create_test(desc)
        test_3 = models_factory.create_test(desc)

        # Assert
        self.assertEqual(1, test_1.id)
        self.assertEqual(2, test_2.id)
        self.assertEqual(3, test_3.id)


class CreateGroup_Should(TestCase):
    def test_createValidGroupInstance(self):
        # Arrange
        name = 'test name'
        models_factory = ModelsFactory()

        # Act
        group = models_factory.create_group(name)

        # Assert
        self.assertIsInstance(group, TestGroup)
        self.assertEqual(1, group.id)
        self.assertEqual(name, group.name)
        self.assertEqual((), group.tests)

    def test_createGroupsWithConsecutiveIds(self):
        # Arrange
        name = 'test name'
        models_factory = ModelsFactory()

        # Act
        group_1 = models_factory.create_group(name)
        group_2 = models_factory.create_group(name)
        group_3 = models_factory.create_group(name)

        # Assert
        self.assertEqual(1, group_1.id)
        self.assertEqual(2, group_2.id)
        self.assertEqual(3, group_3.id)


class CreateTestRun_Should(TestCase):
    def test_createValidTestRunInstance(self):
        # Arrange
        valid_result = 'pass'
        valid_runtime_ms = '5'
        models_factory = ModelsFactory()

        # Act
        test_run = models_factory \
            .create_test_run(valid_result, valid_runtime_ms)

        # Assert
        expected_test_result = TestResult(valid_result)
        expected_runtime_ms = int(valid_runtime_ms)

        self.assertIsInstance(test_run, TestRun)
        self.assertEqual(expected_test_result, test_run.test_result)
        self.assertEqual(expected_runtime_ms, test_run.runtime_ms)

    def test_raiseError_invalidTestResultFormat(self):
        # Arrange
        valid_runtime_ms = '5'
        models_factory = ModelsFactory()

        # Act ^ Assert
        with self.assertRaises(ApplicationError):
            test_run = models_factory \
                .create_test_run('Invalid', valid_runtime_ms)

    def test_raiseError_invalidRuntimeMsFormat(self):
        # Arrange
        valid_result = 'pass'
        models_factory = ModelsFactory()

        # Act ^ Assert
        with self.assertRaises(ApplicationError):
            test_run = models_factory \
                .create_test_run(valid_result, 'Invalid')
