"""
Project Euler Problem 24: Lexicographic Permutations

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
"""

import functools

NUM_OF_DIGITS = 10
TARGET = 1000000


def solve():
    """Solve Project Euler Problem 24."""
    results = []
    digits = [digit for digit in range(10)]
    target = TARGET

    for i in range(NUM_OF_DIGITS):
        blocks = factorial(NUM_OF_DIGITS - i - 1)
        # find max k such that K * blocks < target
        k = 0
        while k * blocks < target:
            k += 1
        index = k - 1
        results.append(digits[index])
        digits = digits[:index] + digits[index + 1 :]
        target -= blocks * index

    return results


@functools.cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
