"""
Project Euler Problem 16: Power Digit Sum

What is the sum of the digits of the number 2^1000
"""


def solve():
    """
    Solve Project Euler Problem 16.

    Obviously we aren't going to multiply the digits out!
    It would need 1000 bits to store the number.

    This problem made me learn the algorithm: double dabble

    let's try to implement!
    """
    # this is so much faster wow
    # return sum([int(c) for c in str(1 << 1000)])
    result = double_dabble([1] + [0] * 1000)
    return sum(result)


def double_dabble(bits: list[int]) -> list[int]:
    # allocate enough for digits
    n = len(bits)
    digits = [0] * (n + 4 * n // 3 + 1)

    # for each bit
    for i in range(n):
        carry = bits[i]
        for j in range(len(digits) - 1, -1, -1):
            digits[j] <<= 1
            digits[j] += carry
            carry = (digits[j] & 16) >> 4
            digits[j] &= 15

        if i == n - 1:
            break
        for j in range(len(digits)):
            if digits[j] >= 5:
                digits[j] += 3
    return digits
