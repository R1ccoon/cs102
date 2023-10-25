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
    alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in plaintext:
        if i in alphabet:
            ciphertext += alphabet[(alphabet.find(i) + shift) % len(alphabet)]
        elif i in alphabet_big:
            ciphertext += alphabet_big[(alphabet_big.find(i) + shift) % len(alphabet_big)]
        else:
            ciphertext += i
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
    alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in ciphertext:
        if i in alphabet:
            plaintext += alphabet[(alphabet.find(i) - shift)]
        elif i in alphabet_big:
            plaintext += alphabet_big[(alphabet_big.find(i) - shift)]
        else:
            plaintext += i
    return plaintext
