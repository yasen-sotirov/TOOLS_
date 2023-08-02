from commands.add_to_category import AddToCategoryCommand

from commands.create_category import CreateCategoryCommand
from commands.create_product import CreateProductCommand

from commands.show_category import ShowCategoryCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    # проверява дали зададената команда отговаря на установените
    def create(self, input_line: str):
        # създава инстанция на команда спрямо cmd и if-else 
        cmd, *params = input_line.split()
        try:
            if cmd.lower() == "createcategory":
                # създава инстанция към съответния клас команда
                # минаваме само през init и подаваме към engine
                command = CreateCategoryCommand(params, self._app_data)
                return command
            
            if cmd.lower() == "createproduct":
                return CreateProductCommand(params, self._app_data)
            
            if cmd.lower() == "showcategory":
                return ShowCategoryCommand(params, self._app_data)
            
            if cmd.lower() == "addproducttocategory":
                return AddToCategoryCommand(params, self._app_data)
            
            # ако не влезе в никой от if-те, вдига грешка 
            raise ValueError
        
        # грешката се изпълнява от except блока
        except ValueError:
            print(f'Command {cmd} is not supported.')
            # и се връща назад към Engine
