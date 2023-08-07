# class SimpleClass:
#     def __init__(self):
#         pass
#
#     def some_method(self):
#         return "This is a method of SimpleClass."
#
#
#
# simple_class_obj_1 = SimpleClass()
#
#
# result = simple_class_obj_1.some_method()
# print(result)


# from errors.invalid_location_error import InvalidLocationError
# try:
#     a = int(input())
# except:
#     raise InvalidLocationError("=====")


# from map_info.locations import Locations
# from errors.invalid_location_error import InvalidLocationError
#
# def view_package(location: str):
#     try:
#         _ = Locations(location.upper())
#     except:
#         raise InvalidLocationError(f"This location is not supported")
#
#
# new_location = view_package("sof")
# print(new_location)