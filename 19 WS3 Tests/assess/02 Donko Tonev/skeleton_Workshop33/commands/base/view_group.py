from commands.base.base_command import BaseCommand

class ViewGroup(BaseCommand):
    def execute(self):
        test_group_id = int(self.params[0])

        test_group = self.app_data.find_test_group_by_id(test_group_id)
        if test_group is None:
            raise ValueError(f"TestGroup with id {test_group_id} not found.")

        report = f"#{test_group.id}. {test_group.name} ({len(test_group.tests)} tests)\n"

        for test in test_group.tests:
            report += f"  #{test.id}. [{test.description}]: {len(test.test_runs)} runs\n"

        return report
