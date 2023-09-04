"ТИПИЗАЦИЯ"  # type hinting


from typing import Union

x_var: str | None   # pipe не се поддържа по в 3,7
y_var: Union[str, None]