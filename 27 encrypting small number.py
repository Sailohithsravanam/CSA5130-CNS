# Public key
e = 17
n = 3233  # assume large in real case

# Build encryption dictionary (simulate attacker)
encrypt_dict = {pow(m, e, n): m for m in range(26)}

# Example ciphertext from Alice (encrypted 'A', 'B', 'C')
ciphertext = [pow(m, e, n) for m in [0, 1, 2]]

# Attacker decrypts using dictionary
decrypted = [encrypt_dict[c] for c in ciphertext]
letters = [chr(m + ord('A')) for m in decrypted]

print("Ciphertext:", ciphertext)
print("Decrypted letters:", letters)
