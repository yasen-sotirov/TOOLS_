from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        toothpaste_name = self._params[0]
        if self._app_data.product_exists(toothpaste_name):
            raise ValueError(f'Toothpaste with name {toothpaste_name} already exists!')

        brand = self._params[1]

        price = self._params[2]
        try_parse_float(price)

        gender = self._params[3]
        Gender.from_string(gender)

        ingredients = self._params[4]

        self._app_data.create_toothpaste(toothpaste_name, brand, price, gender, ingredients)

        return f'Toothpaste with name {toothpaste_name} was created!'
