from commands.base.base_command import BaseCommand

class ViewSystem(BaseCommand):
    def execute(self):
        report = f"Test Reporter System ({len(self.app_data.groups)} test groups)\n"

        for group in self.app_data.groups:
            report += f"  #{group.id}. {group.name} ({len(group.tests)} tests)\n"
            for test in group.tests:
                report += f"    #{test.id}. [{test.description}]: {len(test.test_runs)} runs\n"

        return report
