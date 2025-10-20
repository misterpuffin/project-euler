"""
Project Euler Problem 12: Highly Divisible Triangular Number

What is the value of the first triangle number to have over five hundred divisors?
Note: The n-th triangle number = 1 + 2 + ... + n
"""

import functools
import math
from typing import Callable


def solve():
    """
    Solve Project Euler Problem 12.

    Each triangle number represented by n(n + 1) / 2
    """

    for n in range(20000):
        if n % 2 == 0:
            d = divisors(n // 2) * divisors(n + 1)
        else:
            d = divisors(n) * divisors((n + 1) // 2)
        if d > 500:
            return n * (n + 1) / 2


@functools.cache
def divisors(n: int):
    get_prime = make_get_prime()

    index = 0
    counter = 0
    result = 1
    while n > 1:
        prime = get_prime(index)
        if n % prime == 0:
            counter += 1
            n //= prime
        else:
            result *= counter + 1
            counter = 0
            index += 1

    return result * (counter + 1)


def make_get_prime() -> Callable[[int], int]:
    primes = [2, 3, 5, 7]
    counter = 7

    def is_prime(n: int):
        if n < 2:
            return False
        for prime in primes:
            if prime > math.isqrt(n):
                return True
            if n % prime == 0:
                return False
        return True

    def get_prime(n: int) -> int:
        nonlocal counter
        while len(primes) < n:
            counter += 2
            if is_prime(counter):
                primes.append(counter)

        return primes[n - 1]

    return get_prime
