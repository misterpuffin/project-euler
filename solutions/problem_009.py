"""
Project Euler Problem 9: Special Pythagorean Triplet

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""


def solve():
    """
    Solve Project Euler Problem 9.

    Revised my number theory notes on Pythagorean Triplets to see if anything would be useful..
    Hoping to learn some new math with this one :)
    """

    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(f"{a} + {b} + {c} = 1000")
                return a * b * c

    return 0
