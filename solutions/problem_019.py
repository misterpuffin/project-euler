"""
Project Euler Problem 19: Counting Sundays

- 1 Jan 1900 was a Monday.
- Thirty days has September,
- April, June and November.
- All the rest have thirty-one,
- Saving February alone,
- Which has twenty-eight, rain or shine.
- And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

MAP = {
    True: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    False: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
}


def solve():
    """Solve Project Euler Problem 19."""
    # Naive solution (am lazy):
    current_start = 1  # Monday
    result = 0
    for year in range(1901, 2001):
        months = MAP[is_leap_year(year)]
        for month in months:
            if current_start == 6:
                result += 1
            current_start += month
            current_start %= 7
    return result


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
