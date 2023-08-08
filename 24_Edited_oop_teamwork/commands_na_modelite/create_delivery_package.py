from core.app_data import ApplicationData
from commands_na_modelite.base_command.base_command_class import BaseCommand
from core.validation_params_methoods import validation_param_count
from models_nai_malkite_elementi_na_programata.customer import Customer
from models_nai_malkite_elementi_na_programata.pakage import Package
from core.date_time import DateTime


class CreateDeliveryPackage(BaseCommand):
    unique_package_id = 2001    # брояч съхраняващ ID -та
    unique_customer_id = 3001

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

        # импортиран метод от модул validation_params_method
        validation_param_count(params, 8)

    def execute(self):
        start_location = self.params[0]
        end_location = self.params[1]
        weight = self.params[2]
        customer_first_name = self.params[3]
        customer_last_name = self.params[4]
        customer_email = self.params[5]
        customer_phone = self.params[6]
        time_stamp = self.params[7]


        # създава новo ID
        CreateDeliveryPackage.unique_package_id += 1

        # присвоява създаденото ИД
        customer_id = self.unique_customer_id

        # създава нов клиент
        new_customer = Customer(customer_id, customer_first_name, customer_last_name, customer_email, customer_phone)

        # създава новo ID
        CreateDeliveryPackage.unique_customer_id +=1

        # присвоява създаденото ИД
        package_id = self.unique_package_id

        time_stamp = time_stamp

        # създава нова пратка
        new_package = Package(package_id, start_location, end_location, weight, customer_id)

        # подава новосъздаденият обект към метода на app_data
        output = self.app_data.add_package_to_system(new_package)

        # връща новосъздаденият обект към app_data
        return output






















