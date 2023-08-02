from base.base_command import BaseCommand

class ViewGroup(BaseCommand):
    def execute(self):
        test_group_id = int(self._params[0])
        test_group = self._app_data.find_test_group_by_id(test_group_id)  # Use find_test_group_by_id method

        if test_group:
            group_id = test_group.id
            group_name = test_group.name
            tests_count = len(test_group.tests)

            test_info = "\n".join(
                f"  #{test.id}. [{test.description}]: {len(test.test_runs)} runs"
                for test in test_group.tests
            )

            report = (
                f"#{group_id}. {group_name} ({tests_count} tests)\n"
                f"{test_info}"
            )
            return report

        return f"Group with id #{test_group_id} not found"