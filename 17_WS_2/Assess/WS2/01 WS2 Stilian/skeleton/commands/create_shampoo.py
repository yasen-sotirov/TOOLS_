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
        s_name = self._params[0]
        s_brand = self._params[1]
        s_price = try_parse_float(self._params[2])
        s_gender = Gender.from_string(self._params[3])
        s_milliliters = try_parse_int(self._params[4])
        s_usage_type = UsageType.from_string(self._params[5])

        if self._app_data.product_exists(s_name):
            raise ValueError(f'Shampoo with name {s_name} already exists!')

        self._app_data.create_shampoo(s_name, s_brand, s_price, s_gender, s_milliliters,
                                      s_usage_type)
        return f'Shampoo with name {s_name} was created!'
