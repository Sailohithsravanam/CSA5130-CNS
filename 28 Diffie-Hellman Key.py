# Prime q and primitive root a
q = 23
a = 5

# Secret keys (private)
xA = 6  # Alice's secret
xB = 15  # Bob's secret

# Public keys
A = pow(a, xA, q)
B = pow(a, xB, q)

# Shared secret key
KA = pow(B, xA, q)
KB = pow(A, xB, q)

print("Alice's key:", KA)
print("Bob's key  :", KB)
