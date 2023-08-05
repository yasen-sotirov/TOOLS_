from errors.validation_param_error import ValidationParamError
# модул, където събира два метода за валидация


def validation_param_count(params, count: int):
    if len(params) != count:
        raise ValidationParamError(f"Invalid number of arguments")


def try_pars_int(value):
    try:
        return int(value)

    except:
        raise ValueError("Invalid value. Should be an integer")