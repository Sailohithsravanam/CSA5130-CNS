from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Key and IV
key = DES3.adjust_key_parity(get_random_bytes(24))  # 3DES 24-byte key
iv = get_random_bytes(8)                            # 3DES block size is 8 bytes

# Plaintext input
plaintext = b"Encrypt this secret message using 3DES CBC mode"

# Padding to 8-byte blocks
padded = pad(plaintext, 8)

# Create 3DES CBC cipher
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Encrypt
ciphertext = cipher.encrypt(padded)

# Output
print("Key       :", key.hex())
print("IV        :", iv.hex())
print("Ciphertext:", ciphertext.hex())
