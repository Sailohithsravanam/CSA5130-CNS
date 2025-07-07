# Mapping from ciphertext symbols to letters (known from Poe's riddle solution)
substitution_map = {
    '5': 't', '3': 'h', '‡': 'e', '†': 'a', '3': 'h', '0': 'r',
    ')': 's', '6': 'o', '*': 'n', ';': 'd', '4': 'i', '8': 'l',
    '2': 'c', '(': 'f', '9': 'u', '1': 'y', ':': 'm', '?': 'b',
    '[': 'w', ']': 'v', '—': 'g', '¶': 'p'
}

ciphertext = ("53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:"
              "‡*8†83  (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956"
              "*2(5*—4)8¶8*  ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;"
              "48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;"
              ":188;‡?;")

# Decrypt using the substitution map
plaintext = ""
for char in ciphertext:
    if char in substitution_map:
        plaintext += substitution_map[char]
    else:
        plaintext += char  # keep unchanged if not in map

print("Decrypted text (partially):")
print(plaintext)
