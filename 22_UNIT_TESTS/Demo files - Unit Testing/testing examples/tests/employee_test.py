import unittest
from src.employee import Employee


class Constructor_Should(unittest.TestCase):
    def test_set_attributes(self):
        employee = Employee('John', 500, 'Finance')

        self.assertEqual('John', employee.full_name)
        self.assertEqual(500, employee.salary)
        self.assertEqual('Finance', employee.department)

    def test_fail_with_valueerror(self):
        with self.assertRaises(ValueError):
            e = Employee('John', 499, 'Finace')


class SalarySetter_Should(unittest.TestCase):
    def test_change_salary(self):
        employee = Employee('John', 500, 'Finance')
        employee.salary = 800
        self.assertEqual(800, employee.salary)

    def test_fail_with_valueerror(self):
        with self.assertRaises(ValueError):
            employee = Employee('John', 800, 'Finance')
            employee.salary = 300


class Info_Should(unittest.TestCase):
    def test_create_correct_text(self):
        employee = Employee('John', 500, 'Finance')
        txt = employee.info()
        self.assertEqual('John, Department: Finance', txt)
