def create_matrix(key):
    key = key.lower().replace('j', 'i')
    seen = []
    for c in key + 'abcdefghijklmnopqrstuvwxyz':
        if c not in seen and c.isalpha():
            seen.append(c)
    return [seen[i:i+5] for i in range(0, 25, 5)]

def preprocess(text):
    text = text.lower().replace('j', 'i')
    cleaned = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if not a.isalpha():
            i += 1
            continue
        if not b.isalpha() or a == b:
            cleaned += a + 'x'
            i += 1
        else:
            cleaned += a + b
            i += 2
    if len(cleaned) % 2 != 0:
        cleaned += 'x'
    return cleaned

def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def encrypt_pair(a, b, matrix):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_encrypt(plaintext, keyword):
    matrix = create_matrix(keyword)
    formatted = preprocess(plaintext)
    ciphertext = ''
    for i in range(0, len(formatted), 2):
        ciphertext += encrypt_pair(formatted[i], formatted[i+1], matrix)
    return ciphertext

# Input
keyword = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")
ciphertext = playfair_encrypt(plaintext, keyword)

# Output
print("Encrypted message:", ciphertext)
