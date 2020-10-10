# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

from typing import List


def longest_pal(s: List):
    if not s:
        return ""

    n = len(s)
    dp = [[0]*n for _ in range(n)]

    # fill for length 1 and 2
    for idx in range(n):
        dp[idx][idx] = 1
    for idx in range(1, n):
        dp[idx-1][idx] = int(s[idx-1] == s[idx])

    # fill rest of the table
    for l in range(3, n+1):
        i = 0
        while i < n+1-l:
            j = i+l-1
            dp[i][j] = int(dp[i+1][j-1] and s[i] == s[j])
            i += 1

    ans = 1
    for i in range(n):
        for j in range(n):
            if dp[i][j]:
                ans = max(ans, j-i+1)
            print(dp[i][j], end=" ")
        print()

    return ans    
    

if __name__ == "__main__":
    a = ["geeks","forgeeksskeegfor"]

    for a_ in a:
        print(longest_pal(list(a_)))
