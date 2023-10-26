import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse

class CalculatorTestCase(unittest.TestCase):

    def test_is_prime1(self):
        self.assertEqual(is_prime(7), True)

    def test_is_prime2(self):
        self.assertEqual(is_prime(11), True)
    
    def test_is_prime3(self):
        self.assertEqual(is_prime(41), True)

    def test_gcd1(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_gcd2(self):
        self.assertEqual(gcd(3, 7), 1)

    def test_inverse1(self):
        self.assertEqual(multiplicative_inverse(25, 72), 49)

    def test_inverse2(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

