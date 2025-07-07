# Left shift schedule for 16 rounds
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

# Function to perform circular left shift
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Select 24 bits from a 28-bit half (simulating PC-2)
def select_24_from_28(bits):
    # Just select positions for simplicity
    return bits[:24]

# Generate subkeys: 48 bits = 24 from left half + 24 from right half
def generate_subkeys(key_56bit):
    C = key_56bit[:28]  # Left 28 bits
    D = key_56bit[28:]  # Right 28 bits
    subkeys = []

    for shift in SHIFT_SCHEDULE:
        # Apply left shifts
        C = left_shift(C, shift)
        D = left_shift(D, shift)

        # Select 24 bits from each half
        part1 = select_24_from_28(C)
        part2 = select_24_from_28(D)

        subkey = part1 + part2
        subkeys.append(subkey)

    return subkeys

# Example usage
if __name__ == "__main__":
    # Example 56-bit key (without parity bits)
    key_56 = '00010011001101000101011101111001100110111011110011011111'

    subkeys = generate_subkeys(key_56)

    print("Generated 16 Subkeys (48-bit each):")
    for i, k in enumerate(subkeys, 1):
        print(f"K{i:02}: {k}")
