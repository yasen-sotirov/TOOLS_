from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        while True:
            try:
                input_line = input().strip()
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                result = command.execute()
                if result:
                    output.append(result)
            except ValueError as err:
                output.append(str(err))

        print('\n'.join(output))