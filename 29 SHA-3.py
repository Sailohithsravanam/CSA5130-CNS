import random

def random_nonzero_lane():
    # Ensure at least one bit is non-zero
    while True:
        value = random.getrandbits(64)
        if value != 0:
            return value

# Initialize SHA-3 state: 25 lanes (64-bit each)
state = [0] * 25

# Capacity lanes: last 9 lanes (index 16 to 24)
capacity_indices = list(range(16, 25))

blocks = 0

while any(state[i] == 0 for i in capacity_indices):
    blocks += 1
    # Create new block of 1024 bits = 16 lanes
    new_block = [random_nonzero_lane() for _ in range(16)]
    
    # XOR new block into the state
    for i in range(16):
        state[i] ^= new_block[i]

print("Number of blocks until all capacity lanes become non-zero:", blocks)
