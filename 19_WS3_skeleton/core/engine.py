from core.command_factory import CommandFactory


class Engine:
    def __init__(self, command_factory: CommandFactory):
        self._command_factory = command_factory

    def start(self):
        output = []

        while True:
            input_line = input()
            if input_line.lower() == 'end':
                break
            command = self._command_factory.create_command(input_line)
            output.append(command.execute())

        print('\n'.join(output))
