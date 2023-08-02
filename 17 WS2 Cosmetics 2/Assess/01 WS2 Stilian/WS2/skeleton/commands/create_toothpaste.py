from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        t_name = self._params[0]
        t_brand = self._params[1]
        t_price = self._params[2]
        t_gender = self._params[3]
        t_ingredients = self._params[4]

        if self._app_data.product_exists(t_name):
            raise ValueError(f'Toothpaste with name {t_name} already exists!')

        Gender.from_string(t_gender)

        try_parse_float(t_price)

        self._app_data.create_toothpaste(t_name, t_brand, t_price, t_gender, t_ingredients)
        return f'Toothpaste with name {t_name} was created!'
