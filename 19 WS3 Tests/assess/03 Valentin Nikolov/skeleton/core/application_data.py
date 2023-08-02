
from models.test_group import TestGroup
from models.test import Test


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []
        self._tests_id_tracker = 0
        self._groups_id_tracker = 0

    @property
    def groups(self):
        return tuple(self._test_groups)

    @property
    def tests_id_tracker(self):
        return self._tests_id_tracker

    @tests_id_tracker.setter
    def tests_id_tracker(self, value):
        self._tests_id_tracker = value

    @property
    def groups_id_tracker(self):
        return self._groups_id_tracker

    @groups_id_tracker.setter
    def groups_id_tracker(self, value):
        self._groups_id_tracker = value

    def add_test_group(self, test_group: TestGroup):
        self._test_groups.append(test_group)

    def find_test_group_by_id(self, id) -> TestGroup:
        for test_group in self.groups:
            if id == test_group.id:
                return test_group

        raise ValueError(f'No Test Group with id:{id} found')

    def find_test_by_id(self, id) -> Test:
        for test_group in self.groups:
            for test in test_group.tests:
                if id == test.id:
                    return test

        raise ValueError(f'No Test with id:{id} found')

    def remove_test_group_by_id(self, id):
        test_group = self.find_test_group_by_id(id)
        for test in test_group.tests:
            test._test_runs.clear()
        test_group._tests.clear()
        self._test_groups.remove(self.find_test_group_by_id(id))
