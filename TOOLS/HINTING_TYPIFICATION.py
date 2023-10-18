"ТИПИЗАЦИЯ"  # type hinting




"ДОК НА ВСИЧКИ ПИТОНСКИ ПАКЕТИ"
# https://pypi.org/


" === PYDANTIC ==="
# https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr--__tabbed_1_2
from pydantic import BaseModel, constr, conint




"ОГРАНИЧЕНИЯ CONstr CONint"
class Project(BaseModel):
    id: int | None = None                       # str или None, по подразбиране None
    name: constr(min_length=1)                  # ограничава дължината
    status: constr(pattern="^open | closed$")   # regex: (^) започва с.  ($) няма нищо след
    limit: conint(ge=1)                         # (ge=) = greater or equal
    devs: list = []





"UNION"
# from typing import Union
# x_var: str | None = None
# y_var: Union[str, None]     # старата версия





"TYPE HINTS / ANNOTATIONS"
# задава типа данни на променливата, ако въведем друго гърми
# ако не зададем нищо принтва предварително зададената ст-ст: 5, abc
# def fnk_1(var_1: int = 5, var_2: str | None = None):
#     print(var_1, var_2)
# fnk_1(1, "abc")
# fnk_1()









