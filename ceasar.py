def encrypt_caesar(plaintext):
    # """
    # Encrypts plaintext using a Caesar cipher.
    #
    # >>> encrypt_caesar("PYTHON")
    # 'SBWKRQ'
    # >>> encrypt_caesar("python")
    # 'sbwkrq'
    # >>> encrypt_caesar("Python3.6")
    # 'Sbwkrq3.6'
    # >>> encrypt_caesar("")
    # ''
    # """
    # PUT YOUR CODE HERE
    ciphertext = ""
    for i in range(len(plaintext)):
        if (65 <= (ord(plaintext[i])) <= 90):
            ciphertext += chr(65 + (ord(plaintext[i]) - 65 + 3) % 26)
        elif (97 <= (ord(plaintext[i])) <= 122):
            ciphertext += chr(97 + (ord(plaintext[i]) - 97 + 3) % 26)
        else:
            ciphertext += plaintext[i]
    print(ciphertext)
    return ciphertext


def decrypt_caesar(ciphertext):
#     """
#     Decrypts a ciphertext using a Caesar cipher.
#
#     >>> decrypt_caesar("SBWKRQ")
#     'PYTHON'
#     >>> decrypt_caesar("sbwkrq")
#     'python'
#     >>> decrypt_caesar("Sbwkrq3.6")
#     'Python3.6'
#     >>> decrypt_caesar("")
#     ''
#     """
#     # PUT YOUR CODE HERE
    plaintext = ""
    for i in range(len(ciphertext)):
        if (65 <= (ord(ciphertext[i])) <= 90):
            plaintext += chr(65 + (ord(ciphertext[i]) - 65 - 3) % 26)
        elif (97 <= (ord(ciphertext[i])) <= 122):
            plaintext += chr(97 + (ord(ciphertext[i]) - 97 - 3) % 26)
        else:
            plaintext += ciphertext[i]
    print(plaintext)
    return plaintext

encrypt_caesar("PYTHON")
encrypt_caesar("python")
encrypt_caesar("Python3.6")
encrypt_caesar("")
decrypt_caesar("SBWKRQ")
decrypt_caesar("sbwkrq")
decrypt_caesar("Sbwkrq3.6")
decrypt_caesar("")
