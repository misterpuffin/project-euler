"""
Project Euler Problem 15: Lattice Paths

Starting in the top left corner of a 2 x 2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are tere through a 20 x 20 grid?
"""


def solve():
    """
    Solve Project Euler Problem 15.

    Approach is just to use choose.
    40 C 20 should be the answer (if I can remember the formula...)
    """

    return choose(40, 20)


def choose(n: int, r: int) -> int:
    """n! / r! (n - r)!"""
    if r < n - r:
        return choose(n, n - r)

    result = 1
    for i in range(r + 1, n + 1):
        result *= i
        result //= i - r  # this is safe! (source: trust me bro)

        # jk, but to explain:
        # since we start with 1,
        # by the time we reach 2 we would have multiplied by a multiple of 2
        # similar for 3, 4, .. and so on

    return result
