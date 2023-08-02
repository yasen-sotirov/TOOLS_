
from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory
        self._results = []

    def start(self):
        while True:
            input_line = input().strip()
            if input_line.lower() == "end":
                break

            try:
                command = self._command_factory.create(input_line)
                result = command.execute()
                self._results.append(result)
            except Exception as e:
                self._results.append(str(e))

        for result in self._results:
            print(result)
