def polyalphabetic_encrypt(plaintext, keyword):
    plaintext = plaintext.lower().replace(' ', '')
    keyword = keyword.lower()
    ciphertext = ''
    key_len = len(keyword)

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('a')
        k = ord(keyword[i % key_len]) - ord('a')
        c = (p + k) % 26
        ciphertext += chr(c + ord('a'))
    
    return ciphertext

# Input
plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

# Output
encrypted = polyalphabetic_encrypt(plaintext, keyword)
print("Encrypted message:", encrypted)
