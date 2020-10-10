# https://www.geeksforgeeks.org/chocolate-distribution-problem/
# Choose k window from sorted array

from typing import List


def min_diff(arr: List, window: int):
    if not arr or not window:
        return 0

    n = len(arr)
    if window > n:
        return -1

    arr.sort()
    i = 0
    j = i + window - 1
    ans = arr[j] - arr[i]

    while j+1 < n:
        i += 1
        j += 1
        ans = min(ans, arr[j] - arr[i])

    return ans


if __name__ == "__main__":
    a = [[7, 3, 2, 4, 9, 12, 56], [3, 4, 1, 9, 56, 7, 9, 12], [12, 4, 7, 9, 2, 23, 25, 41,
30, 40, 28, 42, 30, 44, 48, 43, 50]]
    m = [3, 5, 7]

    for a_, m_ in zip(a, m):
        print(min_diff(a_, m_))
