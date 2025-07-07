def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd_val, x, y

# Sample RSA public key
n = 3599         # n = p * q (we don't know p, q yet)
e = 31           # public exponent
m = 59           # plaintext block with common factor with n

# Step 1: Check gcd
g = gcd(m, n)

if g != 1:
    print(f"Found factor of n: p = {g}")
    p = g
    q = n // p
    print(f"q = {q}")

    # Step 2: Compute φ(n)
    phi = (p - 1) * (q - 1)

    # Step 3: Compute private key d
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    print(f"Private key d = {d}")
else:
    print("No common factor found, can't factor n.")
