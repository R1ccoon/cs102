import unittest
from src.lab1.calculator import calculator


class TestCalculator(unittest.TestCase):
    # setUp method is overridden from the parent class TestCas

    # Each test method starts with the keyword test_
    def test_add(self):
        self.assertEqual(calculator('4+7'), 11)

    def test_subtract(self):
        self.assertEqual(calculator('7-3'), 4)

    def test_multiply(self):
        self.assertEqual(calculator('3*7'), 21)

    def test_divide(self):
        self.assertEqual(calculator('10//5'), 2)

    def test_bad_input(self):
        m = ['exit()', 'akasdkas', '01e2ke0', 'qdl']
        for i in m:
            self.assertEqual(calculator(i), 'Неверный формат ввода')

    def test_zero_division(self):
        self.assertEqual(calculator('10/0'), 'Деление на ноль')


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
