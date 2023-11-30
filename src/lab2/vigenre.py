def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(plaintext)):
        shift = ord(keyword[i % len(keyword)].lower()) - 97
        if plaintext[i].lower() in alphabet:
            if plaintext[i].islower():
                if ord(plaintext[i]) + shift > 122:
                    ciphertext += chr(ord(plaintext[i]) + shift - 26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + shift)
            elif plaintext[i].isupper():
                if ord(plaintext[i]) + shift > 90:  # кодировка последней заглавной буквы в латинице
                    ciphertext += chr(ord(plaintext[i]) + shift - 26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + shift)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(ciphertext)):
        shift = ord(keyword[i % len(keyword)].lower()) - 97
        if ciphertext[i].lower() in alphabet:
            if ciphertext[i].islower():
                if ord(ciphertext[i]) - shift < 97:
                    plaintext += chr(ord(ciphertext[i]) - shift + 26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - shift)
            elif ciphertext[i].isupper():
                if ord(ciphertext[i]) - shift < 65:  # кодировка последней заглавной буквы в латинице
                    plaintext += chr(ord(ciphertext[i]) - shift + 26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext += ciphertext[i]
    return plaintext

