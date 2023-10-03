"ТИПИЗАЦИЯ"  # type hinting


from typing import Union

x_var: str | None   # pipe не се поддържа по в 3,7
y_var: Union[str, None]





"TYPE HINTS / ANNOTATIONS"
# задава типа данни на променливата, ако въведем друго гърми
# var_1: int = 5
# var_2: str = "abc"
# dict_1: dict[str, int] = {}
# lst_1: list[str] = []

# „|“  стойността е или|или


"ГЕНЕРИРАНЕ НА ТИПОВЕ"
from typing import TypeVar, List
# Дефинираме типова променлива T,
# която може да бъде str или int
# T = TypeVar('T', str, int)
# def print_elements(lst: List[T]) -> None:
#     for element in lst:
#         print(element)
#
# # Използваме функцията със списъци от типове str и int
# str_list = ['a', 'b', 'c', 'd']
# int_list = [1, 2, 3, 4, 5]
#
# print_elements(str_list)  # Изпечатва: a b c d
# print_elements(int_list)  # Изпечатва: 1 2 3 4 5


