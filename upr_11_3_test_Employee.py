import unittest
from upr_11_3_Employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""
    def setUp(self):
        self.user = Employee('oleg','kanevsky')

    def test_give_default_raise(self):
        self.user.give_raise()

    def test_give_custom_raise(self):
        self.user.give_raise()


unittest.main()