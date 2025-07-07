def to_num(c): return ord(c) - ord('a')
def to_char(n): return chr(n % 26 + ord('a'))

def encrypt(text, key):
    text = text.replace(" ", "").lower()
    return ''.join(to_char(to_num(c) + key[i]) for i, c in enumerate(text))

def recover_key(cipher, text):
    cipher, text = cipher.lower(), text.replace(" ", "").lower()
    return [(to_num(c) - to_num(t) + 26) % 26 for c, t in zip(cipher, text)]

# (a) Encrypt
plain1 = "send more money"
key1 = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
cipher = encrypt(plain1, key1)

# (b) Recover key
plain2 = "cash not needed"
key2 = recover_key(cipher, plain2)

print("Encrypted Ciphertext:", cipher)
print("Recovered Key:", key2)
