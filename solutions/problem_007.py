"""
Project Euler Problem 7: 10 001st Prime

What is the 10001st prime number?
"""


def solve():
    """Solve Project Euler Problem 7."""

    primes = []

    def is_prime(num: int) -> bool:
        for prime in primes:
            if num % prime == 0:
                return False
        primes.append(num)
        return True

    curr = 2
    while len(primes) < 10001:
        is_prime(curr)
        curr += 1

    return primes[-1]
