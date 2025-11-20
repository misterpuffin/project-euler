"""
Project Euler Problem 26: Reciprocal Cycles

Find the value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal fraction part
"""


def solve():
    """
    Solve Project Euler Problem 26.

    I learnt this! in Number Theory I'm pretty sure. Continued fraction or something.
    Not sure how it's helpful here
    """
    max_so_far = 0
    candidate = 1
    for i in range(1, 1000):
        result = cycle(1, i)
        max_so_far = max(max_so_far, result)
        if result == max_so_far:
            candidate = i

    return candidate


def cycle(numerator: int, denominator: int) -> int:
    """
    Given a fraction, determine the length of the cycle
    """

    table = {0: 0}  # hash table to store if we last saw a remainder

    remainder = numerator
    i = 0
    while remainder not in table:
        table[remainder] = i
        i += 1

        while remainder < denominator:
            remainder *= 10

        remainder %= denominator
        if remainder == 0:
            return 0

    return i - table[remainder]
