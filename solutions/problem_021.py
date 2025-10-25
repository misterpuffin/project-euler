"""
Project Euler Problem 21: Amicable Numbers

Evaluate the sum of all amicable numbers under 1000
"""

import functools


def solve():
    """Solve Project Euler Problem 21."""
    result = 0
    for i in range(1, 10001):
        if i == d(d(i)) and i != d(i):
            result += i

    return result


@functools.cache
def d(n: int) -> int:
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result
