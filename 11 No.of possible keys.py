import math

# Total number of letters used in Playfair cipher (I and J combined)
n = 25

# Calculate 25!
total_keys = math.factorial(n)

# Convert total keys to power of 2
log2_total_keys = math.log2(total_keys)

# Consider effective unique keys by dividing by 2 (I=J equivalence)
effective_keys = total_keys // 2
log2_effective_keys = math.log2(effective_keys)

# Display results
print(f"Total possible keys (25!): {total_keys}")
print(f"Approximate as power of 2: 2^{log2_total_keys:.2f}")

print(f"\nEffectively unique keys (25!/2): {effective_keys}")
print(f"Approximate as power of 2: 2^{log2_effective_keys:.2f}")
