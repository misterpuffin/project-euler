"""
Project Euler Problem 25: 1000-digit Fibonacci Number

What is the index of the first term in the Fibonacci sequence to contain 1000 digits
"""

import math


def solve():
    """Solve Project Euler Problem 25."""
    index = 1
    a = 0
    b = 1

    while math.log10(b) < 999:
        tmp = a
        a = b
        b += tmp
        index += 1

    return index
