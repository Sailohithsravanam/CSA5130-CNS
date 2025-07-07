def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "No modular inverse, invalid key"
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# Frequency guesses:
# Ciphertext: B -> E (1 → 4), U -> T (20 → 19)

# Solve: 
# E1 = (a * 4 + b) % 26 = 1
# E2 = (a * 19 + b) % 26 = 20

# => Two equations:
# a*4 + b ≡ 1 mod 26
# a*19 + b ≡ 20 mod 26

# Subtract: (19a - 4a) ≡ 19 (mod 26)
# => 15a ≡ 19 (mod 26)
# => Solve for a

for a in range(1, 26, 2):  # a must be coprime to 26
    if mod_inverse(a, 26):
        if (15 * a) % 26 == 19:
            b = (1 - a * 4) % 26
            print(f"Found key: a = {a}, b = {b}")
            sample_cipher = "BUEBUUBZ"  # example ciphertext
            print("Decrypted text:", affine_decrypt(sample_cipher, a, b))
            break
