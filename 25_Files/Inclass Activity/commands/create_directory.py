from commands.base.base_command import BaseCommand
import os

class CreateDirectoryCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 1)
        self.params = params

    def execute(self):
        # създава папка
        dir_name = self.params[0]
        try:
            os.mkdir(f"demo_folder/{dir_name}")

        # ако съществува, вдига грешка
        except OSError as err:
            print(err)


