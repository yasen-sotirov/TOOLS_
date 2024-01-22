"UNIT TEST "    # https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
                # Инес:   https://softuni.bg/trainings/resources/video/70483/video-25-march-2022-ines-kenova-python-oop-february-2022/3591

"""
UNIT TEST
    автоматизирано тестване на парче код - Unit
    проверяват коректността на unit of work
    unit of work - част от функциолността, която не може да бъде раздробена на по-малки парчета
    
    
3A PATTERN    
    Arrange - създаваме инстанция на юнита, който ще тестваме
    Act     - частта, която тества юнита
    Assert  - проверка на резултата. един или много
    
    
БРОЙ ASSERT
    Един тест тества една функционалност. Повече assertion са ок 
    ако са логически свързани с тестваната функционалност. 
    
    
FRAMEWORK   "unittest"
    Помага ни с готови функционалности:
    - стартиране на на един или много тестове едновременно
    - готови функции (assertion)
    - връща статистики от проведените тестове
    
    
ИМЕНУВАНЕ
    - класове CamelCase_Should
    - методите test_whatTestReturn_onWhichConditions
    
    
ASSERT METHODS
    assertEqual(a, b)	        a == b
    assertNotEqual(a, b)	    a != b
    assertTrue(x)	            bool(x) is True
    assertFalse(x)	            bool(x) is False
    assertIs(a, b)	            a is b
    assertIsNot(a, b)	        a is not b
    assertIsNone(x)	            x is None
    assertIsNotNone(x)	        x is not None
    assertIn(a, b)	            a in b
    assertNotIn(a, b)	        a not in b
    assertIsInstance(a, b)	    isinstance(a, b)
    assertNotIsInstance(a, b)	not isinstance(a, b)

    assertRaises(ValueError, func, a, b)

"""


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, money):
        if money <= 0:
            raise ValueError('salary must be positive number')
        self._salary = money



"===== TESTS ====="

from unittest import TestCase
class Employee_Should(TestCase):

    def test_fail_with_value_error_negative_salary(self):
        with self.assertRaises(ValueError):
            employee = Employee('John', -500)



from unittest import TestCase




#
#
# class Worker:
#     def __init__(self, name:str, salary: int, energy: int):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'
#
#
#
# # ==== TESTS =====
#
# class WorkerTest(TestCase):
#     def test_worker_is_initialized_correctly(self):
#         # Arrange - приготвя данните
#         # Act - действие
#         worker_1 = Worker("Test", 1500, 10)
#
#         #Assert - проверява дали нещата са се случили
#         self.assertEqual("Test", worker_1.name)
#






# from unittest.mock import Mock
#
# from datetime import datetime
#
# tuesday = datetime(2023, 11, 2)
# saturday = datetime(2023, 11, 4)
#
# datetime = Mock()
#
# def  is_weekday():
#     today = datetime.today()
#     day_of_week = today.weekday()
#     return 0 <= day_of_week < 5
#
# datetime.today.return_value = tuesday
#
#
# import requests
#
# def get_holidays():
#     r = requests.get('http://localhost/api/holidays')
#     if r.status_code == 200:
#         return r.json()
#     return None
#
# # class TestGetHolidays(TestCase):
# #     def test_get_holidays_connection():
# #         pass
#
#
#
# if __name__ == '__main__':
#     print(get_holidays())
#
#
#
#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()
