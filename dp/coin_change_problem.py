# https://www.geeksforgeeks.org/coin-change-dp-7/

from typing import List


def num_of_ways(coins: List, val: int):
    coins.sort()
    n = len(coins)

    dp = [[0]*(n+1) for _ in range(val+1)]
    for idx in range(n+1):
        dp[0][idx] = 1

    for v in range(1, val+1):
        for j in range(1, n+1):
            # count of solutions including coin j
            x = dp[v-coins[j-1]][j] if v >= coins[j-1] else 0 

            # excluding coin j
            y = dp[v][j-1]

            dp[v][j] = x + y

    # for v in range(val+1):
    #     for j in range(n+1):
    #         print(dp[v][j], end=" ")
    #     print()

    return dp[val][n]

if __name__ == "__main__":
    c = [[1,2,3],[2,3,5,6],
    [1, 5, 6, 9], [25, 10, 5]
    ]
    v = [4, 10,
     9, 30
     ]

    for c_, v_ in zip(c, v):
        print(num_of_ways(c_, v_))
