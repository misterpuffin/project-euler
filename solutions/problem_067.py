"""
Project Euler Problem 18: Maximum Path Sum II

Fund the maximum total from top to bottom in triangle.txt
"""


def solve():
    """Solve Project Euler Problem 18."""

    TRIANGLE = load_triangle("data/0067_triangle.txt")

    n = len(TRIANGLE)
    dp = [[0] * (i + 1) for i in range(n)]  # maximum path from that index

    dp[n - 1] = TRIANGLE[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + TRIANGLE[i][j]

    return dp[0][0]


def load_triangle(path: str):
    result = []
    with open(path, "r") as file:
        for line in file:
            result.append(list(map(int, line.split(" "))))

    return result
