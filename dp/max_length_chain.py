# https://www.geeksforgeeks.org/maximum-length-chain-of-pairs-dp-20/
# variation of LIS

from typing import List


def longest_chain(arr: List):
    arr.sort()
    n = len(arr)
    ans = [1]*n

    for idx in range(n):
        for j in range(idx):
            if arr[idx][0] > arr[j][1] and ans[idx] < ans[j] + 1:
                ans[idx] = ans[j] + 1
    
    return max(ans)


if __name__ == "__main__":
    a = [[(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)],
    [(6,8),(3,4)]]

    for a_ in a:
        print(longest_chain(a_))