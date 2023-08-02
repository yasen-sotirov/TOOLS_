from base.base_command import BaseCommand

class ViewSystem(BaseCommand):
    def execute(self):
        test_groups_count = len(self._app_data.groups)
        groups_info = "\n".join(
            f"  #{group.id}. {group.name} ({len(group.tests)} tests)"
            for group in self._app_data.groups
        )

        report = (
            f"Test Reporter System ({test_groups_count} test groups)\n"
            f"{groups_info}"
        )
        return report