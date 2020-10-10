# https://www.geeksforgeeks.org/longest-common-substring-dp-29/

from typing import List


def lc_substring(s1: str, s2: str):
    m = len(s1)
    n = len(s2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    res = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                print(i-1, j-1, s1[i-1], s2[j-1])
                dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
                res = max(res, dp[i][j])
            else:
                # dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
                dp[i][j] = 0

    for i in range(m+1):
        for j in range(n+1):
            print(dp[i][j], end=" ")
        print()

    return res


if __name__ == "__main__":
    a = ["GeeksforGeeks", "abcdxyz", "zxabcdezy"]
    b = ["GeeksQuiz", "xyzabcd", "yzabcdezx"]

    for a_, b_ in zip(a, b):
        print(lc_substring(a_, b_))
