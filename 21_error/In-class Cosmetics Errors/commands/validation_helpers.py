def try_parse_float(float_string: str, msg: str):
    try:
        return float(float_string)
    except:
        raise ValueError(msg)
    

def validate_params_count(params, count):
    if len(params) != count:
        raise ValueError(
            f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")')

