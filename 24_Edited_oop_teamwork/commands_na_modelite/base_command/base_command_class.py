from core.app_data import ApplicationData

class BaseCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        # втория параметър, който трябва да се подаде е обект от Application Data
        self.params = params
        self.app_data = app_data


base_command_object_1 = BaseCommand(["param 1", "param 2"], ApplicationData)