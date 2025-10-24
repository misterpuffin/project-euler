"""
Project Euler Problem 17: Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""


def solve():
    """Solve Project Euler Problem 17."""

    sum = 0
    sum += len("one") * 9 * 10
    sum += len("two") * 9 * 10
    sum += len("three") * 9 * 10
    sum += len("four") * 9 * 10
    sum += len("five") * 9 * 10
    sum += len("six") * 9 * 10
    sum += len("seven") * 9 * 10
    sum += len("eight") * 9 * 10
    sum += len("nine") * 9 * 10

    sum += len("ten") * 10
    sum += len("eleven") * 10
    sum += len("twelve") * 10
    sum += len("thirteen") * 10
    sum += len("fourteen") * 10
    sum += len("fifteen") * 10
    sum += len("sixteen") * 10
    sum += len("seventeen") * 10
    sum += len("eighteen") * 10
    sum += len("nineteen") * 10

    sum += len("twenty") * 10 * 10
    sum += len("thirty") * 10 * 10
    sum += len("forty") * 10 * 10
    sum += len("fifty") * 10 * 10
    sum += len("sixty") * 10 * 10
    sum += len("seventy") * 10 * 10
    sum += len("eighty") * 10 * 10
    sum += len("ninety") * 10 * 10

    sum += len("onehundredand") * 100
    sum += len("twohundredand") * 100
    sum += len("threehundredand") * 100
    sum += len("fourhundredand") * 100
    sum += len("fivehundredand") * 100
    sum += len("sixhundredand") * 100
    sum += len("sevenhundredand") * 100
    sum += len("eighthundredand") * 100
    sum += len("ninehundredand") * 100

    """ NO AND FOR EACH FIRST HUNDRED """
    sum -= len("and") * 9

    sum += len("onethousand")
    return sum
