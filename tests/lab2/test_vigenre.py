import string
import unittest
import random

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt1(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')

    def test_encrypt2(self):
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')

    def test_encrypt3(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')
    
    def test_decrypt1(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')
    
    def test_decrypt2(self):
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')
    
    def test_decrypt3(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))
    