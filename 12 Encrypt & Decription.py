import numpy as np

def char_to_num(c):
    return ord(c) - ord('a')

def num_to_char(n):
    return chr((n % 26) + ord('a'))

def preprocess(text):
    text = text.replace(" ", "").lower()
    if len(text) % 2 != 0:
        text += 'x'  # pad if odd
    return text

def encrypt_hill(text, key_matrix):
    text = preprocess(text)
    encrypted = ""
    for i in range(0, len(text), 2):
        pair = [char_to_num(text[i]), char_to_num(text[i+1])]
        result = np.dot(key_matrix, pair) % 26
        encrypted += num_to_char(result[0]) + num_to_char(result[1])
    return encrypted

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt_hill(ciphertext, key_matrix):
    det = int(np.round(np.linalg.det(key_matrix)))
    det_mod_inv = mod_inverse(det % 26, 26)
    
    if det_mod_inv is None:
        raise ValueError("Matrix not invertible mod 26")

    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                         [-key_matrix[1][0], key_matrix[0][0]]])
    
    inv_matrix = (det_mod_inv * adjugate) % 26

    decrypted = ""
    for i in range(0, len(ciphertext), 2):
        pair = [char_to_num(ciphertext[i]), char_to_num(ciphertext[i+1])]
        result = np.dot(inv_matrix, pair) % 26
        decrypted += num_to_char(result[0]) + num_to_char(result[1])
    return decrypted

# Given key
key_matrix = np.array([[9, 4],
                       [5, 7]])

# Message
message = "meet me at the usual place at ten rather than eight oclock"

# Encrypt
cipher = encrypt_hill(message, key_matrix)
print("Encrypted:", cipher)

# Decrypt
decrypted = decrypt_hill(cipher, key_matrix)
print("Decrypted:", decrypted)
