def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result

# Input
message = input("Enter message: ")
k = int(input("Enter shift (1-25): "))
encrypted = caesar_cipher(message, k)
print("Encrypted message:", encrypted)
