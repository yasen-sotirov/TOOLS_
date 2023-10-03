
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    # методът е извикан от main.py
    def start(self):

        # събира всички подадени команди
        output_list = []
        
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'exit':
                    break
                
                # променливата command е референция към инстация на някоя от командите според подадени 
                # input лине 
                command = self._command_factory.create(input_line)
                # правилната команда вече е създадена 

                # изпълняваме execute метода на командата
                result = command.execute()  # връща съобщениет от изпълнение на execute метода
                output_list.append(result)    

            except Exception as error:
                
                output_list.append(error.args[0]) 
            
                       
        print('\n'.join(output_list))

