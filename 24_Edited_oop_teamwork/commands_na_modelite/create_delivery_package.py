from core.app_data import ApplicationData
from commands_na_modelite.base_command.base_command_class import BaseCommand
from core.validation_params_methoods import validation_param_count


class CreateDeliveryPackage(BaseCommand):
    unique_package_id = 2001    # брояч съхраняващ ID -та
    unique_customer_id = 3001

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

        # импортиран метод от модул validation_params_method
        validation_param_count(params, 7)

    def execute(self):
        print("=== The delivery package is created ===")



