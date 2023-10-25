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
    for i in range(len(plaintext)):
        shift = ord(keyword[i % len(keyword)].lower()) - 97
        if ord(plaintext.lower()[i]) + shift > 122:
            ciphertext += chr(ord(plaintext.lower()[i]) + shift - 26)
        else:
            ciphertext += chr(ord(plaintext.lower()[i]) + shift)
    if plaintext[0].isupper():
        ciphertext = ciphertext.upper()
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
    for i in range(len(ciphertext)):
        shift = ord(keyword[i % len(keyword)].lower()) - 97
        if ord(ciphertext.lower()[i]) - shift < 97:
            plaintext += chr(ord(ciphertext.lower()[i]) - shift + 26)
        else:
            plaintext += chr(ord(ciphertext.lower()[i]) - shift)
    if ciphertext[0].isupper():
        plaintext = plaintext.upper()

    return plaintext

