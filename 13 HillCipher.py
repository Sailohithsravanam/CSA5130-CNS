import numpy as np

def mod_inverse(a, m):
    """ Modular inverse of a under mod m """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, modulus):
    """ Modular inverse of a 2x2 matrix under mod 26 """
    det = int(np.round(np.linalg.det(matrix)))
    det = det % modulus
    inv_det = mod_inverse(det, modulus)
    if inv_det is None:
        raise ValueError("Matrix is not invertible under mod", modulus)

    # Adjugate matrix
    adj = np.array([[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]])
    
    inv_matrix = (inv_det * adj) % modulus
    return inv_matrix

def known_plaintext_attack(plaintext_pairs, ciphertext_pairs):
    P = np.array(plaintext_pairs).T
    C = np.array(ciphertext_pairs).T

    print("Plaintext matrix P:\n", P)
    print("Ciphertext matrix C:\n", C)

    P_inv = matrix_mod_inverse(P, 26)
    print("Inverse of Plaintext matrix mod 26:\n", P_inv)

    K = np.dot(C, P_inv) % 26
    return K

def char_to_num(c):
    return ord(c.lower()) - ord('a')

# Example:
# Let's assume plaintext: "he", "ll", "ow" → maps to numerical pairs
# And ciphertext: "RI", "JZ", "TA"

plaintext_pairs = [
    [char_to_num('h'), char_to_num('l')],
    [char_to_num('e'), char_to_num('l')]
]

ciphertext_pairs = [
    [char_to_num('r'), char_to_num('j')],
    [char_to_num('i'), char_to_num('z')]
]

K = known_plaintext_attack(plaintext_pairs, ciphertext_pairs)
print("Recovered Key Matrix K:\n", K)
