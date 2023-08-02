from models.test_group import TestGroup
from models.test import Test

class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)

    def add_test_group(self, test_group: TestGroup):
        self._test_groups.append(test_group)

    def find_test_group_by_id(self, test_group_id: int) -> TestGroup:
        for group in self._test_groups:
            if group.id == test_group_id:
                return group

    def remove_test_group(self, test_group_id: int):
        group_to_remove = self.find_test_group_by_id(test_group_id)
        if group_to_remove:
            self._test_groups.remove(group_to_remove)

    def find_test_by_id(self, test_id: int) -> Test:
        for group in self._test_groups:
            for test in group.tests:
                if test.id == test_id:
                    return test