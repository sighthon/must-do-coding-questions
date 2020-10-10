# geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# variation of lis

from typing import List


def min_jumps(arr: List):
    n = len(arr)
    if arr[0] == 0:
        return 10**10

    dp = [10**10]*n
    dp[0] = 0
    dp[1] = 1

    for idx in range(2, n):
        for j in range(idx):
            if idx - j <= arr[j]:
                dp[idx] = min(dp[idx], dp[j]+1) 

    print(dp)
    return dp[n-1]

if __name__ == "__main__":
    a = [[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    for a_ in a:
        print(min_jumps(a_))