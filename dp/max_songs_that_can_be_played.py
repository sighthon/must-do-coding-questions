# geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# variation of lis

from typing import List


def max_songs(arr: List, time: int):
    arr.sort()
    n = len(arr)
    dp = [[0]*(time+1) for _ in range(n+1)]

    for idx in range(time+1):
        dp[0][idx] = 0
    for idx in range(n+1):
        dp[idx][0] = 0

    for idx in range(1, n+1):
        for t in range(1, time+1):
            if t < arr[idx-1]:
                dp[idx][t] = dp[idx-1][t]
            else:
                dp[idx][t] = max(dp[idx-1][t], 1 + dp[idx-1][t-arr[idx-1]])

    for idx in range(n+1):
        for t in range(time+1):
            print(dp[idx][t], end=" ")
        print()
    
    return dp[n][time]


if __name__ == "__main__":
    a = [[2, 4, 3, 5, 5, 2, 4], [2, 4, 3, 5, 5, 2, 4, 3]]
    b = [20, 20]

    for a_, b_ in zip(a, b):
        print(max_songs(a_, b_))