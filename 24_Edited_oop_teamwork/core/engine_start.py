"""
Чете Input-a
подава input-a  на command_factory
събира изпълнените команди в списък
спира програмата при команда end

"""
from core.command_factory import CommandFactory


class Engine:
    # този клас го ползваме само заради методите
    def __init__(self, factory: CommandFactory):
        self.command_factory = factory

    def start(self):
        # събира всички команди
        output_list: list[str] = []
        while True:
            input_line = input()
            if input_line.lower() == "end":
                break

            # подава input в command factory на метода create
                            # прикачена е към променлива за да я добави командата към списъка с команди
            command = self.command_factory.create(input_line)

            # създадената команда я изпълнява
            # съхранява командата в списъка
            output_list.append(command.execute())
















