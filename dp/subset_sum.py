# geeksforgeeks.org/subset-sum-problem-dp-25/

from typing import List


def subset_sum(arr: List, val: int):
    n = len(arr)
    dp = [[False]*(val+1) for _ in range(n+1)]

    for idx in range(1, val+1):
        dp[0][idx] = False
    for idx in range(n+1):
        dp[idx][0] = True

    for i in range(1, n+1):
        for v in range(1, val+1):
            if arr[i-1] > v:
                dp[i][v] = dp[i-1][v]
            else:
                dp[i][v] = dp[i-1][v] or dp[i-1][v-arr[i-1]]

    for i in range(n+1):
        for v in range(val+1):
            print(dp[i][v], end=" ")
        print(" ")
    
    return dp[n][val]


if __name__ == "__main__":
    c = [[3, 34, 4, 12, 5, 2], [3, 34, 4, 12, 5, 2]]
    v = [9, 34]

    for c_, v_ in zip(c, v):
        print(subset_sum(c_, v_))
