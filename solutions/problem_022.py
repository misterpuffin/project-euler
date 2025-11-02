"""
Project Euler Problem 22: Names Scores

What is the total of all the name scores in the file?
"""


def solve():
    """Solve Project Euler Problem 22."""
    with open("data/0022_names.txt", "r") as file:
        data = file.read()
        names = data.split(",")
        names = [name.strip('"') for name in names]
        names.sort()

        result = 0
        for i, name in enumerate(names):
            score = sum((ord(c) - 64) for c in name)
            result += score * (i + 1)
        return result
