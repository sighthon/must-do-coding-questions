# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# variation of LIS

from typing import List


def lis(arr: List):
    n = len(arr)

    ans = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                ans[i] = max(ans[i], ans[j] + 1)

    return max(ans)


if __name__ == "__main__":
    a = [[10, 22, 9, 33, 21, 50, 41, 60, 80],
    [3, 10, 2, 1, 20],
    [3,2],
    [50, 3, 10, 7, 40, 80]]

    for a_ in a:
        print(lis(a_))