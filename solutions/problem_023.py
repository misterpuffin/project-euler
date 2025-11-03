"""
Project Euler Problem 23: Non-Abundant Sums

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
"""

import functools


def primes(n: int) -> list[int]:
    """Generate primes up to n using Sieve of Eratosthenes."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [num for num in range(2, n + 1) if is_prime[num]]


ALL_PRIMES = primes(28123)


def solve():
    """Solve Project Euler Problem 23."""
    numbers = list(abundant(28123))
    n = len(numbers)

    ls = [False] * 28123

    for i in range(n):
        for j in range(i, n):
            curr = numbers[i] + numbers[j]
            if curr <= 28123:
                ls[curr - 1] = True

    return sum(i for i in range(1, 28124) if not ls[i - 1])


def abundant(n: int) -> set[int]:
    """Find all abundant numbers up to n."""
    result = set()
    for i in range(1, n + 1):
        if sum_of_proper_divisors(i) > i:
            result.add(i)
    return result


@functools.cache
def sum_of_proper_divisors(n: int) -> int:
    """
    Calculate sum of proper divisors using prime factorization.
    Uses the formula: for n = p1^a1 * p2^a2 * ...,
    sum of divisors = product of (p^(a+1) - 1)/(p - 1) for each prime p.
    """
    divisors = prime_divisors(n)
    result = 1
    for prime in divisors:
        power = divisors[prime]
        result *= ((prime ** (power + 1)) - 1) // (prime - 1)

    return result - n


def prime_divisors(n: int) -> dict[int, int]:
    """Get prime factorization as dict of prime -> power."""
    result = {}
    for prime in ALL_PRIMES:
        if prime * prime > n:
            break
        while n % prime == 0:
            if prime not in result:
                result[prime] = 1
            else:
                result[prime] += 1
            n //= prime
    if n > 1:
        result[n] = 1
    return result

