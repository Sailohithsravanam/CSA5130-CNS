def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for c in key:
        if c not in seen and c.isalpha():
            seen.add(c)
            matrix.append(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            seen.add(c)
            matrix.append(c)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None, None

def decrypt_digraph(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair(ciphertext, key):
    matrix = generate_matrix(key)
    ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""

    for digraph in digraphs:
        if len(digraph) == 2:
            plaintext += decrypt_digraph(matrix, digraph[0], digraph[1])
    return plaintext

# Main code
cipher = """KXJEY UREBE ZWEHE WRYTU HEYFS 
KREHE GOYFI WTTTU OLKSY CAJPO 
BOTEI ZONTX BYBNT GONEY CUZWR 
GDSON SXBOU YWRHE BAAHY USEDQ"""

cipher = cipher.replace('\n', ' ').replace('  ', ' ')
key = "MONARCHY"  # Example key; historical key is unknown

decrypted = decrypt_playfair(cipher, key)
print("Decrypted Text:\n", decrypted)
