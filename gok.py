# test_employee.py
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """
        Create an employee instance to use in all test methods.
        This ensures we don’t have to create a new employee in each test method.
        """
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        """Test that the default raise of $5000 is applied correctly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test that a custom raise amount is applied correctly."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
