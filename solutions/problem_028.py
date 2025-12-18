"""
Project Euler Problem 28: Number Spiral Diagonals

What is the sum of the numbers on the diagonals in
a 1001 by 1001 spiral form in the same way?
"""


def solve():
    """Solve Project Euler Problem 28."""
    # let's just aim to count in O(n)
    return spiral(1001)


def spiral(size: int) -> int:
    # size should be odd
    n = size // 2
    curr = 1
    result = 1
    for i in range(n):
        for _ in range(4):
            curr += (i + 1) * 2
            result += curr
    return result
