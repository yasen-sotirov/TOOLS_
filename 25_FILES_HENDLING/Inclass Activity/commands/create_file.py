import os
from errors import errors
from commands.base.base_command import BaseCommand


class CreateFileCommand(BaseCommand):

    def __init__(self, params):
        super().__init__(params, 2)
        self.params = params

    def execute(self):
        folder_name, file_name = self.params
        text = "text text\n"
        path = f"demo_folder/{folder_name}/{file_name}"
        demo_folder = f"demo_folder/{folder_name}"

        try:
            if not os.path.isdir(demo_folder):
                raise errors.FolderDoesNotExist
            elif os.path.isfile(file_name):
                raise FileExistsError
            else:
                file = open(path, 'a')
                file.write(text)
                file.close()

        except Exception as err:
            print(err)
