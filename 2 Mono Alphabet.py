def monoalphabetic_cipher(plaintext, cipher_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''
    for char in plaintext.lower():
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += cipher_key[index]
        else:
            ciphertext += char
    return ciphertext

# Fixed cipher key (26 unique letters)
cipher_key = 'phqgiumeaylnofdxjkrcvstzwb'

# Input
plaintext = input("Enter message: ")
encrypted = monoalphabetic_cipher(plaintext, cipher_key)

# Output
print("Encrypted message:", encrypted)
