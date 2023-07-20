from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.scent import Scent


class CreateCreamCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        cream_name = self._params[0]
        if self._app_data.product_exists(cream_name):
            raise ValueError(f'Cream with name {cream_name} already exists!')

        brand = self._params[1]

        price = self._params[2]
        try_parse_float(price)

        gender = self._params[3]
        Gender.from_string(gender)

        scent = self._params[4]
        Scent.from_string(scent)

        return f'Scent with name {cream_name} was created!'

