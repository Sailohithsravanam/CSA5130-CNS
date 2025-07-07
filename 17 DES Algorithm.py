# Simplified DES-style Decryption in Python

def xor(a, b):
    return ''.join(['0' if i == j else '1' for i, j in zip(a, b)])

# Dummy 64-bit initial permutation (does nothing)
def initial_permutation(bits):
    return bits

# Dummy 64-bit inverse permutation (does nothing)
def inverse_permutation(bits):
    return bits

# Dummy key generation: creates 16 round keys from main key
def generate_keys(main_key):
    keys = []
    for i in range(16):
        key = main_key[i:] + main_key[:i]  # Left shift
        keys.append(key[:48])  # Use first 48 bits
    return keys

# DES round function (simplified: just XOR with subkey)
def des_round(right, key):
    return xor(right, key[:len(right)])

# DES decryption using reverse round keys
def des_decrypt(ciphertext, key64):
    keys = generate_keys(key64)
    keys = keys[::-1]  # Reverse the keys for decryption

    # Initial permutation
    block = initial_permutation(ciphertext)
    left, right = block[:32], block[32:]

    for i in range(16):
        temp = right
        right = xor(left, des_round(right, keys[i]))
        left = temp

    # Combine halves in reverse order for final permutation
    combined = right + left
    plaintext = inverse_permutation(combined)
    return plaintext

# Example usage
key64 = '0001001100110100010101110111100110011011101111001101111111110001'  # 64-bit
ciphertext64 = '1000111100011110101010110011001110001100110011111111000000001111'  # 64-bit

plaintext64 = des_decrypt(ciphertext64, key64)
print("Decrypted plaintext (binary):", plaintext64)
