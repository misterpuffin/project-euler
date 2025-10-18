"""
Project Euler Problem 10: Summation of Primes

Find the sum of all the primes below two million.
"""

import math


def solve():
    """Solve Project Euler Problem 10."""
    # Slow but should work
    result = 0
    for i in range(2, 2000000):
        if is_prime(i):
            result += i

    return result


def is_prime(num: int) -> bool:
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True
