from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType


class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        shampoo_name = self._params[0]
        if self._app_data.product_exists(shampoo_name):
            raise ValueError(f'Shampoo with name {shampoo_name} already exists!')

        brand = self._params[1]

        price = self._params[2]
        try_parse_float(price)

        gender = self._params[3]
        Gender.from_string(gender)

        milliliters = self._params[4]
        try_parse_int(milliliters)

        usage_type = self._params[5]
        UsageType.from_string(usage_type)

        self._app_data.create_shampoo(shampoo_name, brand, price, gender, usage_type, milliliters)

        return f'Shampoo with name {shampoo_name} was created!'
