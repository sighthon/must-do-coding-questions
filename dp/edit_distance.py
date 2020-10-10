# https://www.geeksforgeeks.org/edit-distance-dp-5/

from typing import List


def edit_distance(s1: str, s2: str):
    m = len(s1)
    n = len(s2)

    dp = [[10**10]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = j  # all inserts
            elif j == 0:
                dp[i][j] = i  # all inserts
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # current matched, so refer to prev
            else:
                dp[i][j] = min(
                    dp[i][j],
                    1 + dp[i-1][j-1], # replace current and refer to previous
                    1 + dp[i][j-1],
                    1 + dp[i-1][j]
                )
    for i in range(m+1):
        for j in range(n+1):
            print(dp[i][j], end=" ")
        print()

    return dp[m][n]

if __name__ == "__main__":
    a = ["geek", "cat", "sunday"]
    b = ["gesek", "cut", "saturday"]

    for a_, b_ in zip(a, b):
        print(edit_distance(a_, b_))
