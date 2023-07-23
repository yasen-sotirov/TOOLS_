from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float
from models.toothpaste import Toothpaste

class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name = self._params[0]
        brand = self._params[1]
        price = try_parse_float(self._params[2])
        gender = self._params[3]
        ingredients = self._params[4]

        self._app_data.add_product(name, brand, price, gender, ingredients)
        return f'Toothpaste with name {name} was created!'