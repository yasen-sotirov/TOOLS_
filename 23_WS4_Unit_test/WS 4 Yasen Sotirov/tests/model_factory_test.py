from unittest import TestCase
from core.models_factory import ModelsFactory
from models.test import Test
from models.test_group import TestGroup
from models.test_run import TestRun
from models.constants.test_result import TestResult
from errors.application_error import ApplicationError

model_factory_obj = ModelsFactory()



class ModelFactory_should(TestCase):

    def test_createGroup_func_work_correctly(self):
        obj_1 = model_factory_obj.create_group("group_1")
        expected_output_1 = TestGroup(1, "group_1")
        self.assertEqual(expected_output_1.id, obj_1.id)
        self.assertEqual(expected_output_1.name, obj_1.name)

        obj_2 = model_factory_obj.create_group("group_2")
        expected_output_2 = TestGroup(2, "group_2")
        self.assertEqual(expected_output_2.id, obj_2.id)
        self.assertEqual(expected_output_2.name, obj_2.name)


    def test_createTest_func_work_correctly(self):
        obj_1 = model_factory_obj.create_group("group_1")
        expected_output_1 = Test(1, "group_1")
        self.assertEqual(expected_output_1.id, obj_1.id)
        self.assertEqual(expected_output_1.description, obj_1.name)

        obj_2 = model_factory_obj.create_group("group_2")
        expected_output_2 = Test(2, "group_2")
        self.assertEqual(expected_output_2.id, obj_2.id)
        self.assertEqual(expected_output_2.description, obj_2.name)


    def test_create_test_run_func_work_correctly(self):
        obj_1 = model_factory_obj.create_test_run("pass", "5")
        expected_output_1 = TestRun(TestResult.PASS, 5)
        self.assertEqual(expected_output_1.test_result, obj_1.test_result)
        self.assertEqual(expected_output_1.runtime_ms, obj_1.runtime_ms)


    def test_create_test_run_func_raise_error_on_invalid_test_result(self):
        with self.assertRaises(ApplicationError):
            _ = model_factory_obj.create_test_run("bla", "5")

    def test_create_test_run_func_raise_error_on_invalid_test_runtime(self):
        with self.assertRaises(ApplicationError):
            _ = model_factory_obj.create_test_run(TestResult.PASS, "five")
