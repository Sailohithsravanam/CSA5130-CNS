def create_cipher_alphabet(keyword):
    keyword = keyword.upper()
    used = set()
    cipher = []

    # Add unique letters from keyword
    for char in keyword:
        if char not in used and char.isalpha():
            cipher.append(char)
            used.add(char)

    # Add remaining letters from A-Z
    for char in range(ord('A'), ord('Z') + 1):
        if chr(char) not in used:
            cipher.append(chr(char))

    return cipher

def encrypt(plaintext, cipher):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt_map = {alphabet[i]: cipher[i] for i in range(26)}

    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            is_lower = char.islower()
            mapped = encrypt_map[char.upper()]
            encrypted += mapped.lower() if is_lower else mapped
        else:
            encrypted += char
    return encrypted

# --- MAIN ---
keyword = "CIPHER"
cipher = create_cipher_alphabet(keyword)
plaintext = input("Enter plaintext: ")
encrypted_text = encrypt(plaintext, cipher)

print("Cipher alphabet:")
print("Plain : " + " ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print("Cipher: " + " ".join(cipher))
print("Encrypted text:", encrypted_text)
