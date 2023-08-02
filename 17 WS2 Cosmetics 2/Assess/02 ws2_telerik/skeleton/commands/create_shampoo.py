from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType
from models.shampoo import Shampoo

class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name = self._params[0]
        brand = self._params[1]
        price = try_parse_float(self._params[2])
        gender = self._params[3]
        usage_type = self._params[4]
        milliliters = try_parse_int(self._params[5])

        self._app_data.create_shampoo(name, brand, price, gender, usage_type, milliliters)
        if self._app_data.product_exists(name):
            raise ValueError(f'Product with name {name} already exists!')
        return f'Shampoo with name {name} was created!'