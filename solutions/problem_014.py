"""
Project Euler Problem 14: Longest Collatz Sequence

Which starting number, under one million, produces the longest chain?
"""

import functools


def solve():
    """Solve Project Euler Problem 14."""
    result = 1
    max_length = 1
    for n in range(1, 1000000):
        length = collatz_length(n)
        max_length = max(length, max_length)
        if length == max_length:
            result = n

    return result


@functools.cache
def collatz_length(n: int) -> int:
    """Given the starting number, return the length of the collatz sequence"""
    if n == 1:
        return 1
    else:
        return collatz_length(collatz(n)) + 1


def collatz(n: int) -> int:
    """Generates the next number in the Collatz Sequence"""
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1
