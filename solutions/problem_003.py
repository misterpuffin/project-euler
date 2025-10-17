"""
Project Euler Problem 3: Largest Prime Factor

What is the largest prime factor of the number 600851475143?
"""

import math


def solve():
    """Solve Project Euler Problem 3."""
    MAGIC_NUMBER = 600851475143
    MAX_FACTOR = math.isqrt(MAGIC_NUMBER)
    result = 1
    keys = list(range(2, MAX_FACTOR + 1))
    sieve = {key: False for key in keys}  # True if composite

    for key in keys:
        if sieve[key]:
            continue

        # key is a prime here
        if MAGIC_NUMBER % key == 0:
            result = key

        curr = key + key
        # mark all multiples of key as composite
        while curr <= MAX_FACTOR:
            sieve[curr] = True
            curr += key

    return result
