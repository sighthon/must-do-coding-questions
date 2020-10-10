# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/

from typing import List


def form_pal(s: str):
    n = len(s)

    dp = [[0]* n for _ in range(n)]
    # fill len 1 and 2
    for idx in range(n):
        dp[idx][idx] = 0
    for idx in range(1, n):
        dp[idx-1][idx] = int(s[idx-1] != s[idx])

    # fill from len 3
    l = 3
    while l <= n:
        i = 0
        while i <= n-l:
            j = i+l-1
            
            dp[i][j] = dp[i+1][j-1]
            dp[i][j] += 2 if s[i] != s[j] else 0

            i += 1
        l += 1

    # for i in range(n):
    #     for j in range(n):
    #         print(dp[i][j], end=" ")
    #     print()

    return dp[0][n-1]

if __name__ == "__main__":
    a = ["ab", "aa", "abcd", "abcda", "abcde"]

    for a_ in a:
        print(form_pal(a_))
