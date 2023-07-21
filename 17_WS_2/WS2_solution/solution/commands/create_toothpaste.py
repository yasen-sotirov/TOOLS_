from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name, brand, *rest, = self._params

        if self._app_data.product_exists(name):
            raise ValueError(
                f'Product with name {name} already exists!')

        price = try_parse_float(rest[0])
        gender = Gender.from_string(rest[1])
        ingredients = rest[2].split(',')

        self._app_data.create_toothpaste(
            name, brand, price, gender, ingredients)

        return f'Toothpaste with name {name} was created!'
