# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

from typing import List


def min_coins(coins: List, val: int):
    coins.sort()
    dp = [[0]*(len(coins)+1) for _ in range(val+1)]

    for idx in range(len(coins)):
        dp[0][idx] = 0
    for idx in range(val+1):
        dp[idx][0] = 10**10

    for v in range(1, val+1):
        for j in range(1, len(coins)+1):
            if v >= coins[j-1] and dp[v % coins[j-1]][j] != 10**10:
                dp[v][j] = min(v//coins[j-1] + dp[v % coins[j-1]][j], dp[v][j-1])
            else:
                dp[v][j] = dp[v][j-1]

    for v in range(1, val+1):
        for j in range(len(coins)+1):
            print(dp[v][j], end=" ")
        print()

    return dp[v][len(coins)]

if __name__ == "__main__":
    c = [[1, 5, 6, 9], [25,10,5]]
    v = [11, 30]

    for c_, v_ in zip(c, v):
        print(min_coins(c_, v_))
