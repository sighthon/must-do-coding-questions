# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

import sys
from typing import List


def sort_array(arr: List):
    n = len(arr)
    idx_0 = -1
    while idx_0+1 < n and arr[idx_0+1] == 0:
        idx_0 += 1
    idx_2 = n
    while idx_2-1 >=0 and arr[idx_2-1] == 2:
        idx_2 -= 1

    idx = idx_0 + 1
    while idx < idx_2:
        if arr[idx] == 0:
            idx_0 += 1
            arr[idx_0], arr[idx] = arr[idx], arr[idx_0]
        elif arr[idx] == 2:
            idx_2 -= 1
            arr[idx_2], arr[idx] = arr[idx], arr[idx_2]

            if arr[idx] == 0:
                idx_0 += 1
                arr[idx_0], arr[idx] = arr[idx], arr[idx_0]
        
        idx += 1


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    a = [[0, 1, 2, 0, 1, 2], [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]]

    for a_ in a:
        sort_array(a_)
        print(a_)
