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
        name, brand, *rest, = self._params

        if self._app_data.product_exists(name):
            raise ValueError(
                f'Product with name {name} already exists!')

        price = try_parse_float(rest[0])
        gender = Gender.from_string(rest[1])
        milliliters = try_parse_int(rest[2])
        usage_type = UsageType.from_string(rest[3])

        self._app_data.create_shampoo(
            name, brand, price, gender, usage_type, milliliters)

        return f'Shampoo with name {name} was created!'
