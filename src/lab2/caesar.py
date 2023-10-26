def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in plaintext:
        if i.lower() in alphabet:
            if i.islower():
                if ord(i) + shift > 122:  # кодировка последней строчной буквы в латинице
                    ciphertext += chr(ord(i) + shift - 26)
                else:
                    ciphertext += chr(ord(i) + shift)

            elif i.isupper():
                if ord(i) + shift > 90:  # кодировка последней заглавной буквы в латинице
                    ciphertext += chr(ord(i) + shift - 26)
                else:
                    ciphertext += chr(ord(i) + shift)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in ciphertext:
        if i.lower() in alphabet:
            if i.islower():
                if ord(i) - shift < 97:  # кодировка последней строчной буквы в латинице
                    plaintext += chr(ord(i) - shift + 26)
                else:
                    plaintext += chr(ord(i) - shift)

            elif i.isupper():
                if ord(i) - shift < 65:  # кодировка последней заглавной буквы в латинице
                    plaintext += chr(ord(i) - shift + 26)
                else:
                    plaintext += chr(ord(i) - shift)
            else:
                plaintext += i
    return plaintext
