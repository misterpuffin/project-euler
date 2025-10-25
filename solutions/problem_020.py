"""
Project Euler Problem 20: Factorial Digit Sum

Find the sum of the digits in the number 100!
"""

import math


def solve():
    """Solve Project Euler Problem 20."""
    return sum([int(s) for s in str(math.prod(range(1, 101)))])
