# # Standard library imports...
# from unittest.mock import patch
#
# # Third-party imports...
# from nose.tools import assert_is_not_none
#
# # Local imports...
# from services import get_todos
#
#
# def test_getting_todos():
#     mock_get_patcher = patch('services.requests.get')
#
#     # Start patching `requests.get`.
#     mock_get = mock_get_patcher.start()
#
#     # Configure the mock to return a response with an OK status code.
#     mock_get.return_value.ok = True
#
#     # Call the service, which will send a request to the server.
#     response = get_todos()
#
#     # Stop patching `requests.get`.
#     mock_get_patcher.stop()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)


import requests
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock # Части от unittest.mock, които се използват за мокване (заместване на реални обекти с фалшиви) на някои функции и обекти по време на тестването.


# Дефиниране на функцията get_user_data(user_id):
# Функцията прави HTTP GET заявка към http://api.example.com/users/{user_id} и връща JSON отговора.
def get_user_data(user_id):
    response = requests.get(f'http://api.example.com/users/{user_id}')
    return response.json()


# Този клас съдържа методите за тестване на функцията get_user_data.
class TestUserData(TestCase):


    # С помощта на @patch('requests.get') се осигурява, че при извикване на requests.get в теста, той няма да изпраща реални HTTP заявки към уеб API. Вместо това, тази функция ще бъде заменена от мокнат обект (фалшив обект), който се използва за имитиране на реалното поведение.
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        # Създава се мокнат обект mock_response, който представлява отговор от уеб API във формат речник.
        mock_response = Mock()
        response_dict = {"name": 'John', 'email': 'john@example.com'}
        # Имитира се методът json на mock_response, за да връща стойността response_dict.
        mock_response.json.return_value = response_dict
        # Задава се, че извикването на requests.get ще връща mock_response.
        mock_get.return_value = mock_response
        # Извиква се get_user_data(1) и се съхранява резултатът в променливата user_data.
        user_data = get_user_data(1)
        # Проверява се дали requests.get е било извикано с правилния URL (f'http://api.example.com/users/1') с помощта на mock_get.assert_called_with.
        mock_get.assert_called_with(f'http://api.example.com/users/1')
        # След това се проверява дали user_data съвпада с очаквания резултат response_dict чрез self.assertEqual.
        self.assertEqual(user_data, response_dict)

# Проверка дали кода се изпълнява като основна програма чрез if __name__ == '__main__': unittest.main().
if __name__ == '__main__':
    unittest.main()




























