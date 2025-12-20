"""
Project Euler Problem 30: Digit Fifth Powers

Find the sum of all numbers that can be written as the sum of
fifth powers of their digits
"""

MAX = 10000000


def solve():
    """
    Realistically the largest is probably 7 digit numbers
    """
    result = 0
    for i in range(10, MAX):
        curr = sum([digit**5 for digit in digits(i)])
        if curr == i:
            result += i

    return result


def digits(num: int) -> list[int]:
    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10

    return result
