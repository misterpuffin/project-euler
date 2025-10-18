"""
Project Euler Problem 5: Smallest Multiple

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import defaultdict
from typing import DefaultDict

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def solve():
    """Solve Project Euler Problem 5."""
    factors = defaultdict(int)
    for i in range(1, 21):
        factors = merge_dicts(factors, prime_factorize(i))

    result = 1

    for k, v in factors.items():
        result *= k**v

    return result


def prime_factorize(num: int) -> dict[int, int]:
    result: DefaultDict = defaultdict(int)
    for prime in PRIMES:
        while num % prime == 0:
            result[prime] += 1
            num //= prime
    return result


def merge_dicts(d1: dict[int, int], d2: dict[int, int]) -> dict[int, int]:
    keys = d1.keys() | d2.keys()
    result = defaultdict(int)
    for key in keys:
        result[key] = max(d1[key], d2[key])

    return result
