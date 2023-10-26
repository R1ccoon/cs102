import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt1(self):
        self.assertEqual(encrypt_caesar("PYTHON"), 'SBWKRQ')

    def test_encrypt2(self):
        self.assertEqual(encrypt_caesar("python"), 'sbwkrq')

    def test_encrypt3(self):
        self.assertEqual(encrypt_caesar("Python3.6"), 'Sbwkrq3.6')

    def test_decrypt1(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), 'PYTHON')

    def test_decrypt2(self):
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")

    def test_decrypt3(self):
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
    