"""
Project Euler Problem 4: Largest Palindrom Product

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solve():
    """Solve Project Euler Problem 4."""
    result = 1
    for x in range(100, 1000):
        for y in range(100, 1000):
            if is_palindrome(product := x * y):
                result = max(result, product)
    return result


def is_palindrome(num: int) -> bool:
    num_string = str(num)
    return num_string == num_string[::-1]
