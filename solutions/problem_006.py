"""
Project Euler Problem 6: Sum Square Difference

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def solve():
    """Solve Project Euler Problem 6."""
    return sum_of_squares(100) - sum_of_ap(100) ** 2


def sum_of_ap(n: int) -> int:
    """Sum of arithmetic progression (inclusive)"""
    return ((n + 1) * n) // 2


def sum_of_squares(n: int) -> int:
    return (n**2 + n) * (2 * n + 1) // 6
