from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Input and setup
plaintext = b"ExampleBlockText!"  # 16 bytes (2 blocks)
block_size = 8  # 3DES block size
key = DES3.adjust_key_parity(get_random_bytes(24))
iv = get_random_bytes(block_size)

# Always pad with at least one block (1-bit + zeros)
padded = pad(plaintext + b'\x80', block_size)

# ECB Mode
ecb = DES3.new(key, DES3.MODE_ECB)
ecb_ct = ecb.encrypt(padded)

# CBC Mode
cbc = DES3.new(key, DES3.MODE_CBC, iv)
cbc_ct = cbc.encrypt(padded)

# CFB Mode (uses segments = 8 bits here)
cfb = DES3.new(key, DES3.MODE_CFB, iv, segment_size=8)
cfb_ct = cfb.encrypt(padded)

# Output
print("ECB:", ecb_ct.hex())
print("CBC:", cbc_ct.hex())
print("CFB:", cfb_ct.hex())
