from collections import Counter

# English letter frequencies (approximate, normalized)
ENGLISH_FREQ = {
    'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32, 'E': 12.02, 'F': 2.30,
    'G': 2.03, 'H': 5.92, 'I': 7.31, 'J': 0.10, 'K': 0.69, 'L': 3.98,
    'M': 2.61, 'N': 6.95, 'O': 7.68, 'P': 1.82, 'Q': 0.11, 'R': 6.02,
    'S': 6.28, 'T': 9.10, 'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17,
    'Y': 2.11, 'Z': 0.07
}

def preprocess(text):
    return ''.join(filter(str.isalpha, text.upper()))

def decrypt(text, shift):
    return ''.join(chr((ord(c) - 65 - shift) % 26 + 65) for c in text)

def frequency_score(text):
    text_freq = Counter(text)
    total = sum(text_freq.values())
    score = 0
    for char in ENGLISH_FREQ:
        observed = (text_freq.get(char, 0) / total) * 100
        expected = ENGLISH_FREQ[char]
        score += abs(observed - expected)
    return score

def letter_frequency_attack(ciphertext, top_n=10):
    ciphertext = preprocess(ciphertext)
    candidates = []
    
    for shift in range(26):
        decrypted = decrypt(ciphertext, shift)
        score = frequency_score(decrypted)
        candidates.append((score, shift, decrypted))
    
    candidates.sort()
    return candidates[:top_n]

# --- MAIN ---
ciphertext = input("Enter the ciphertext: ")
top_plaintexts = letter_frequency_attack(ciphertext, top_n=10)

print("\nTop 10 probable plaintexts:")
for rank, (score, shift, plain) in enumerate(top_plaintexts, 1):
    print(f"{rank:2}. Shift: {shift:2}, Score: {score:.2f}, Plaintext: {plain}")
