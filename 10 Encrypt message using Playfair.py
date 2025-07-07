matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

def find_position(char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None

def process_text(text):
    text = ''.join([c.upper() for c in text if c.isalpha()])
    text = text.replace('J', 'I')
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            digraphs.append((a, 'X'))
            i += 1
        else:
            digraphs.append((a, b))
            i += 2
    if len(digraphs[-1]) == 1:
        digraphs[-1] = (digraphs[-1][0], 'X')
    return digraphs

def encrypt_digraph(a, b):
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_playfair(message):
    digraphs = process_text(message)
    ciphertext = ''
    for a, b in digraphs:
        ciphertext += encrypt_digraph(a, b)
    return ciphertext

# Main
plaintext = "Must see you over Cadogan West. Coming at once."
ciphertext = encrypt_playfair(plaintext)
print("Encrypted Message:\n", ciphertext)
