from unittest import TestCase
from errors.application_error import ApplicationError
from models.test_group import TestGroup
from models.test import Test


VALID_ID = 5
VALID_DESCRIPTION = "Pesho"



class Test_group_Should(TestCase):

    def test_initializerSetsAttributesCorrectly(self):
        # Arrange
        test_group_1 = TestGroup(VALID_ID, VALID_DESCRIPTION)

        # Act & Assert
        self.assertEquals(VALID_ID, test_group_1.id)
        self.assertEquals(VALID_DESCRIPTION, test_group_1.name)


    def test_constructor_raiseError_when_name_IsNone(self):
        with self.assertRaises(ApplicationError):
            _ = TestGroup(VALID_ID, None)


    def test_constructor_raiseError_when_name_IsEmptyStr(self):
        with self.assertRaises(ApplicationError):
            _ = TestGroup(VALID_ID, "")


    def test_toString_returnsCorrectlyFormattedString(self):
        # Arrange
        test_1 = Test(5, "asdasd")
        test_group_1 = TestGroup(VALID_ID, VALID_DESCRIPTION)
        test_group_1.add_test(test_1)
        expected_output = f"#{VALID_ID}. {VALID_DESCRIPTION} ({len(test_group_1.tests)} tests)"

        #Act & Assert
        self.assertEquals(expected_output, test_group_1.__str__())


    def test_addTestFunc_add_test_to_list(self):
        # Arrange
        test_group_1 = TestGroup(1, "TestGroup")
        test_to_add = Test(VALID_ID, VALID_DESCRIPTION)

        # Act
        test_group_1.add_test(test_to_add)

        # Assert
        self.assertEquals(1, len(test_group_1.tests))


    def test_addTestFunc_check_IdCorrectly(self):
        # Arrange
        test_group_1 = TestGroup(1, "TestGroup")
        test_to_add = Test(VALID_ID, VALID_DESCRIPTION)

        # Act
        test_group_1.add_test(test_to_add)
        test_group_1.add_test(test_to_add)

        # Assert
        self.assertEquals(1, len(test_group_1.tests))


    def test_view_returnCorrectlyFormattedString(self):
        # Arrange
        test_group_1 = TestGroup(1, "TestGroup")

        # Act
        test_group_1.add_test(Test(1, "first"))
        expected_output = '\n'.join([f'{test_group_1}'] + [f'  {test}' for test in test_group_1.tests])

        self.assertEquals(expected_output, test_group_1.view())