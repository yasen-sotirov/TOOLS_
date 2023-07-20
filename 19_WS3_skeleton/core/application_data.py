from models.test_group import TestGroup
from models.test import Test
#  добавя тестова група
#  намира тестова група по id
#  премахва тестова група по id
#  намира тест по id


class ApplicationData:
    groups_id = 0

    def __init__(self):
        self._test_groups: list[TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)

    def create_test_group(self, new_test_group_name):
        # променя IDто
        ApplicationData.groups_id += 1
        new_test_group_id = ApplicationData.groups_id
        # създава нова група тестове
        new_test_group = TestGroup(new_test_group_id, new_test_group_name)
        # добавя новата група към списъка
        self._test_groups.append(new_test_group)
        return f"The group {new_test_group_name} was created."

    def find_test_group_by_id(self, search_test_id):
        for obj in self._test_groups:
            if search_test_id in obj.name:
                return obj
        raise ValueError(f"The group not found.")

    def remove_test_group_by_id(self, search_test_id):
        if self.find_test_group_by_id(search_test_id):
            self._test_groups.remove(self._test_groups[search_test_id])

    def find_test_by_id(self, search_test_id):
        for obj in Test.tests_list:
            if obj.id == search_test_id:
                return obj
        raise ValueError(f"Test not found.")

