"""
Project Euler Problem 2: Even Fibonacci Numbers

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def solve():
    """Solve Project Euler Problem 2."""
    a = 1
    b = 1
    c = a + b
    result = 0
    while c < 4000000:
        if c % 2 == 0:
            result += c
        a, b = b, c
        c += a

    return result
