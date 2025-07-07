from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import copy

def flip_bit(data, byte_index, bit_index):
    # Flip a single bit in a byte at specified index
    flipped = bytearray(data)
    flipped[byte_index] ^= (1 << bit_index)
    return bytes(flipped)

def encrypt_ecb(plaintext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 8))

def decrypt_ecb(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 8)

def encrypt_cbc(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext, 8))

def decrypt_cbc(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), 8)

# Setup
key = DES3.adjust_key_parity(get_random_bytes(24))
iv = get_random_bytes(8)
plaintext = b"MessageBlock1MessageBlock2MessageBlock3"

# ECB encryption and simulate error in ciphertext
ecb_cipher = encrypt_ecb(plaintext, key)
ecb_cipher_error = flip_bit(ecb_cipher, 0, 0)  # flip 1st bit of 1st block
ecb_decrypted_error = decrypt_ecb(ecb_cipher_error, key)

# CBC encryption and simulate error in C1
cbc_cipher = encrypt_cbc(plaintext, key, iv)
cbc_cipher_error = flip_bit(cbc_cipher, 0, 0)  # flip 1st bit of C1
try:
    cbc_decrypted_error = decrypt_cbc(cbc_cipher_error, key, iv)
except ValueError:
    cbc_decrypted_error = b"[Decryption Error: Padding Failed]"

# Print results
print("Original Plaintext:", plaintext)
print("ECB Decrypted (with error in C1):", ecb_decrypted_error)
print("CBC Decrypted (with error in C1):", cbc_decrypted_error)
