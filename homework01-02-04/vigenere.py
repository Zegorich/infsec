def encrypt_vigenere(plaintext, keyword):
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
    n = len(keyword) - 1
    j = -1
    for i in range(len(plaintext)):
        j+=1
        if (65 <= (ord(plaintext[i])) <= 90):
            ciphertext += chr(65 + (ord(plaintext[i]) - 65 + (ord(keyword[j]) - 65)) % 26)
        elif (97 <= (ord(plaintext[i])) <= 122):
            ciphertext += chr(97 + (ord(plaintext[i]) - 97 + (ord(keyword[j]) - 97)) % 26)
        else:
            ciphertext += plaintext[i]
        if j==n:
            j=-1

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
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
    n=len(keyword)-1
    j=-1
    for i in range(len(ciphertext)):
        j+=1
        if (65 <= (ord(ciphertext[i])) <= 90):
            plaintext += chr(65 + (ord(ciphertext[i]) - 65 - (ord(keyword[j]) - 65)) % 26)
        elif (97 <= (ord(ciphertext[i])) <= 122):
            plaintext += chr(97 + (ord(ciphertext[i]) - 97 - (ord(keyword[j]) - 97)) % 26)
        else:
            plaintext += ciphertext[i]
        if j==n:
            j=-1

    return plaintext

# encrypt_vigenere("PYTHON", "A")
# encrypt_vigenere("python", "a")
# encrypt_vigenere("ATTACKATDAWN", "LEMON")
#
# decrypt_vigenere("PYTHON", "A")
# decrypt_vigenere("python", "a")
# decrypt_vigenere("LXFOPVEFRNHR", "LEMON")