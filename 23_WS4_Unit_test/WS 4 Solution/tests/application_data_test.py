from unittest import TestCase

from core.application_data import ApplicationData
from models.test import Test
from models.test_group import TestGroup


class Initializer_Should(TestCase):
    def test_assignEmptyTestGroupsCollection(self):
        # Arrange & Act
        app_data = ApplicationData()

        # Assert
        self.assertEqual((), app_data.groups)


class AddGroup_Should(TestCase):
    def test_returnTrue_whenSuccessfullyAdded(self):
        # Arrange
        app_data = ApplicationData()

        # Act
        result = app_data.add_group(TestGroup(1, 'g1_name'))

        # Assert
        self.assertTrue(result)

    def test_returnFalse_groupWithSameIdExists(self):
        # Arrange
        app_data = ApplicationData()
        same_id = 1
        app_data.add_group(TestGroup(same_id, 'g1_name'))

        # Act
        result = app_data.add_group(TestGroup(same_id, 'g2_name'))

        # Assert
        self.assertFalse(result)

    def test_addTestGroupsToState(self):
        # Arrange
        app_data = ApplicationData()
        g1, g2 = TestGroup(1, 'g1_name'), TestGroup(2, 'g2_name')

        # Act
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Assert
        self.assertEqual((g1, g2), app_data.groups)


class RemoveGroup_Should(TestCase):
    def test_returnTrue_whenCorrectlyRemoved(self):
        # Arrange
        app_data = ApplicationData()
        group_to_remove_id = 3
        g1, g2 = TestGroup(1, 'g1'), TestGroup(group_to_remove_id, 'g2')
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Act
        result = app_data.remove_group(group_to_remove_id)

        # Assert
        self.assertTrue(result)

    def test_returnFalse_whenNoSuchGroup(self):
        # Arrange
        app_data = ApplicationData()
        group_to_remove_id = 1234
        g1, g2 = TestGroup(1, 'g1'), TestGroup(2, 'g2')
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Act
        result = app_data.remove_group(group_to_remove_id)

        # Assert
        self.assertFalse(result)

    def test_returnFalse_whenAppDataIsEmpty(self):
        # Arrange
        app_data = ApplicationData()
        group_to_remove_id = 1234

        # Act
        result = app_data.remove_group(group_to_remove_id)

        # Assert
        self.assertFalse(result)

    def test_removeFromState(self):
        # Arrange
        app_data = ApplicationData()
        group_to_remove_id = 2
        g1 = TestGroup(1, 'g1')
        g2 = TestGroup(group_to_remove_id, 'g2')
        g3 = TestGroup(3, 'g3')
        app_data.add_group(g1)
        app_data.add_group(g2)
        app_data.add_group(g3)

        # Act
        result = app_data.remove_group(group_to_remove_id)

        # Assert
        self.assertEqual((g1, g3), app_data.groups)

    def test_removeFromState_whenOnlyOneGroup(self):
        # Arrange
        app_data = ApplicationData()
        group_to_remove_id = 3
        app_data.add_group(TestGroup(group_to_remove_id, 'g3'))

        # Act
        result = app_data.remove_group(group_to_remove_id)

        # Assert
        self.assertEqual((), app_data.groups)


class FindGroup_Should(TestCase):
    def test_returnGroupByCorrectId(self):
        # Arrange
        app_data = ApplicationData()
        searched_group_id = 2
        g1, g2 = TestGroup(1, 'g1'), TestGroup(searched_group_id, 'g2')
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Act
        group = app_data.find_group(searched_group_id)

        # Assert
        self.assertIsNotNone(group)
        self.assertEqual(searched_group_id, group.id)
        self.assertIsInstance(group, TestGroup)

    def test_notRemoveFromState_whenGroupIsFound(self):
        # Arrange
        app_data = ApplicationData()
        searched_group_id = 2
        g1, g2 = TestGroup(1, 'g1'), TestGroup(searched_group_id, 'g2')
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Act
        group = app_data.find_group(searched_group_id)

        # Assert
        self.assertIsNotNone(group)
        self.assertEqual((g1, g2), app_data.groups)

    def test_returnNone_whenNoGroupWithSuchId(self):
        # Arrange
        app_data = ApplicationData()
        searched_group_id = 2
        g1, g2 = TestGroup(1, 'g1'), TestGroup(3, 'g2')
        app_data.add_group(g1)
        app_data.add_group(g2)

        # Act
        group = app_data.find_group(searched_group_id)

        # Assert
        self.assertIsNone(group)

    def test_returnNone_whenEmptyState(self):
        # Arrange
        app_data = ApplicationData()
        searched_group_id = 2

        # Act
        group = app_data.find_group(searched_group_id)

        # Assert
        self.assertIsNone(group)


class FindTest_Should(TestCase):
    def test_returnTestByCorrectId(self):
        # Arrange
        app_data = ApplicationData()
        searched_test_id = 3
        g1 = TestGroup(1, 'g1')
        g2 = TestGroup(2, 'g1')
        app_data.add_group(g1)
        app_data.add_group(g2)
        g1.add_test(Test(searched_test_id, 'test desc'))
        g2.add_test(Test(1, 'test desc'))

        # Act
        found_test = app_data.find_test(searched_test_id)

        # Assert
        self.assertIsNotNone(found_test)
        self.assertEqual(searched_test_id, found_test.id)
        self.assertIsInstance(found_test, Test)

    def test_returnNone_whenNoGroupHasSuchTest(self):
        # Arrange
        app_data = ApplicationData()
        searched_test_id = 5
        g1 = TestGroup(1, 'g1')
        g2 = TestGroup(2, 'g1')
        app_data.add_group(g1)
        app_data.add_group(g2)
        g1.add_test(Test(1, 'test desc'))
        g2.add_test(Test(2, 'test desc'))

        # Act
        found_test = app_data.find_test(searched_test_id)

        # Assert
        self.assertIsNone(found_test)

    def test_returnNone_whenEmptyState(self):
        # Arrange
        app_data = ApplicationData()
        searched_test_id = 2

        # Act
        found_test = app_data.find_test(searched_test_id)

        # Assert
        self.assertIsNone(found_test)
