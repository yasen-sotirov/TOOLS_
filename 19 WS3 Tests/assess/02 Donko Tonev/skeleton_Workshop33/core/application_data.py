
from models.test_group import TestGroup
from models.test_group import Test


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []
        self._next_test_ids: dict[int, int] = {}

    @property
    def groups(self):
        return tuple(self._test_groups)

    def find_test_group_by_id(self, test_group_id: int) -> TestGroup:
        for group in self._test_groups:
            if group.id == test_group_id:
                return group
        return None
    
    def find_test_by_id(self, test_id: int) -> Test:
        for group in self._test_groups:
            for test in group.tests:
                if test.id == test_id:
                    return test
        return None
    
    def remove_test_group(self, test_group: TestGroup):
        self._test_groups.remove(test_group)


    def generate_next_test_id(self, test_group_id: int) -> int:
        next_test_id = self._next_test_ids.get(test_group_id, 1)  
        self._next_test_ids[test_group_id] = next_test_id + 1  
        return next_test_id
