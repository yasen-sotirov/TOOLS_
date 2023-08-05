from core.app_data import ApplicationData
from commands_na_modelite.create_delivery_package import CreateDeliveryPackage


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self.app_data = data

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        # всяка команда е отделен клас, който го импортваме
        # от папка Commands
        if cmd.lower() == "createdeliverypackage":
            # метод от импортиран модул
            return CreateDeliveryPackage(params, self.app_data)


