from core.application_data import ApplicationData
from commands.validation_helpers import *

# клас, който валидира аргументите и ги подава към App_data
class CreateCategoryCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        # сверява дали подадените аргументи са достатъчни 
        # за инстанциране на обект от съответния клас
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    
    def execute(self):
        # вижда кое е ието на новата категория
        category_name = self._params[0]

        # от метода на app_data проверява дали категорията съществува
        if self._app_data.category_exists(category_name):

            # вдига грешка, която ще се отнесе до try-except блока три нива назад в Engine
            raise ValueError(f'Category {category_name} already exists.')

        # създава съответната категория
        self._app_data.create_category(category_name)
        # връща съобщение
        return f'Category with name {category_name} was created!'
