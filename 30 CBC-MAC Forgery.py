def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def dummy_block_cipher_encrypt(block, key):
    # Simulated fixed cipher for demo: just XOR with key
    return xor(block, key)

def cbc_mac(key, blocks):
    iv = bytes(len(key))  # IV = 0
    prev = iv
    for block in blocks:
        prev = dummy_block_cipher_encrypt(xor(block, prev), key)
    return prev

# Setup
key = b'\x0f\x0f\x0f\x0f'  # 4-byte key
X = b'\xaa\xbb\xcc\xdd'    # One-block message

# Step 1: Legitimate MAC
T = cbc_mac(key, [X])
print("MAC(K, X) =", T.hex())

# Step 2: Adversary forges two-block message: X || (X ⊕ T)
second_block = xor(X, T)
forged_mac = cbc_mac(key, [X, second_block])
print("Forged MAC(X || (X⊕T)) =", forged_mac.hex())

# Check if forgery is successful
print("Forgery valid?", forged_mac == T)
