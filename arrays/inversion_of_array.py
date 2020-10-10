# https://www.geeksforgeeks.org/counting-inversions/

import sys
from typing import List


def merge(arr: List, s: int, m: int, e: int, merged: List):
    ans = 0
    a_idx = s
    b_idx = m+1
    idx = s
    while idx <= e and a_idx <= m and b_idx <= e:
        if arr[b_idx] < arr[a_idx]:
            merged[idx] = arr[b_idx]
            ans += (m-a_idx+1)
            b_idx += 1
        else:
            merged[idx] = arr[a_idx]
            a_idx += 1
        idx += 1

    while idx <= e and a_idx <= m:
        merged[idx] = arr[a_idx]
        a_idx += 1
        idx += 1

    while idx <= e and b_idx <= e:
        merged[idx] = arr[b_idx]
        b_idx += 1
        idx += 1

    for idx in range(s, e+1):
        arr[idx] = merged[idx]

    return ans


def inversion_count(arr: List, s: int, e: int, merged: List):
    ans = 0
    if s >= e:
        return ans

    m = s + (e-s)//2
    ans += inversion_count(arr, s, m, merged)
    ans += inversion_count(arr, m+1, e, merged)
    ans += merge(arr, s, m, e, merged)

    return ans


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    a = [[8, 4, 2, 1], [3, 1, 2]]

    for a_ in a:
        merged = [-1]*len(a_)
        ans = inversion_count(a_, 0, len(a_)-1, merged)
        print(ans)
