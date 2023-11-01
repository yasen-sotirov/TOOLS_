"UNIT TEST "    # https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
                # Инес:   https://softuni.bg/trainings/resources/video/70483/video-25-march-2022-ines-kenova-python-oop-february-2022/3591

"""
    Arrange - приготвя данните
    Act     - действие
    Assert  - проверка на резултата

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




from unittest.mock import Mock

from datetime import datetime

tuesday = datetime(2023, 11, 2)
saturday = datetime(2023, 11, 4)

datetime = Mock()

def  is_weekday():
    today = datetime.today()
    day_of_week = today.weekday()
    return 0 <= day_of_week < 5

datetime.today.return_value = tuesday


import requests

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestGetHolidays(TestCase):
    def test_get_holidays_connection():
        pass



if __name__ == '__main__':
    print(get_holidays())
