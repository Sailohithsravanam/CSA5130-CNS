from collections import Counter

# Standard English letter frequency order
english_freq_order = 'etaoinshrdlucmfwypvbgkjqxz'

def frequency_attack(ciphertext, top_n=10):
    ciphertext = ''.join(filter(str.isalpha, ciphertext.lower()))
    freq = Counter(ciphertext)
    
    # Sort letters in the cipher by frequency
    cipher_freq_order = ''.join([pair[0] for pair in freq.most_common()])
    
    # Generate possible mappings based on frequency alignment
    guesses = []
    for i in range(top_n):
        mapping = str.maketrans(cipher_freq_order, english_freq_order[i:] + english_freq_order[:i])
        possible_plaintext = ciphertext.translate(mapping)
        guesses.append(possible_plaintext)
    
    return guesses

# Sample ciphertext input
cipher = input("Enter cipher text: ")
results = frequency_attack(cipher, top_n=10)

print("\nTop 10 Possible Plaintexts:")
for i, res in enumerate(results, 1):
    print(f"{i}: {res}")
