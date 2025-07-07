def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Bob's known parameters
p = 61
q = 53
n = p * q            # n = 3233
phi = (p - 1)*(q - 1)  # φ(n) = 3120
old_d = 2753         # Bob's old private key (leaked)

# Attacker knows p, q, n, φ(n), and old_d
# Bob chooses a new e, say 17
e_new = 17

# Attacker can compute new private key d
_, d_new, _ = extended_gcd(e_new, phi)
d_new = d_new % phi

print("New private key d:", d_new)
