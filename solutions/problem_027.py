"""
Project Euler Problem 27: Quadratic Primes

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0
"""

import math


def solve():
    """
    Observations:

    - b should be prime > 0
    - should not be factorizable
    """
    # TODO: Implement solution
    bs = primes(1000)
    all_primes = primes(10000)  # some arbitrarily large number
    result = 1, 41
    max_so_far = 40
    for b in bs:
        for a in range(-999, 1000):
            if discriminant(a, b) == 0:
                continue
            chain_length = count(a, b, all_primes)
            if chain_length > max_so_far:
                result = a, b
                max_so_far = chain_length

    return math.prod(result)


def discriminant(a: int, b: int) -> int:
    return b**2 - 4 * a


def count(a, b, all_primes):
    n = 0
    while (n**2 + a * n + b) in all_primes:
        n += 1

    return n


def primes(limit: int) -> set[int]:
    if limit <= 2:
        return set()
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p < limit:
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1
    primes = set(num for num in range(limit) if is_prime[num])
    return primes
