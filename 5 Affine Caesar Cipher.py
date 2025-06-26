import math

def is_valid_a(a):
    return math.gcd(a, 26) == 1

def affine_encrypt(plaintext, a, b):
    if not is_valid_a(a):
        return "Invalid value of 'a'. It must be coprime with 26."

    result = ''
    for char in plaintext.lower():
        if char.isalpha():
            p = ord(char) - ord('a')
            c = (a * p + b) % 26
            result += chr(c + ord('a'))
        else:
            result += char
    return result

# Input
plaintext = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Output
encrypted = affine_encrypt(plaintext, a, b)
print("Encrypted message:", encrypted)
