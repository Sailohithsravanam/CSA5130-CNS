# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

# Step 1: Find p and q such that p * q = n
def find_factors(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None, None

# Given values
e = 31
n = 3599

# Step 2: Find p, q
p, q = find_factors(n)
print("p =", p, ", q =", q)

# Step 3: Compute φ(n)
phi = (p - 1) * (q - 1)

# Step 4: Find private key d such that (d * e) % φ(n) = 1
gcd, d, _ = extended_gcd(e, phi)
d = d % phi  # Make sure d is positive

# Output the private key
print("Private key d =", d)
