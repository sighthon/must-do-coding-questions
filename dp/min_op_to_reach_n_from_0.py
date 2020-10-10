# https://www.geeksforgeeks.org/minimum-cost-to-reach-a-point-n-from-0-with-two-different-operations-allowed/

from typing import List


def min_cost(n: int, p: int, q: int):
    dp = [10**10]*(n+1)
    dp[0] = 0
    dp[1] = p
    for idx in range(2, n+1):
        c1 = dp[idx-1]+p
        c2 = dp[idx//2]+q if idx % 2 == 0 else 10**10
        dp[idx] = min(c1, c2)

    return dp[n]

if __name__ == "__main__":
    n = [1,9]
    p = [3,5]
    q = [4,1]

    for n_, p_, q_ in zip(n, p, q):
        print(min_cost(n_, p_, q_))
