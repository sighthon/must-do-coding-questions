# https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/

from typing import List


def reverse_arr(arr: List, size: int):
    n = len(arr)
    s = 0
    e = min(s + size - 1, n - 1)
    while s < n:
        s_idx = s
        e_idx = e
        while s_idx < e_idx:
            arr[s_idx], arr[e_idx] = arr[e_idx], arr[s_idx]
            s_idx += 1
            e_idx -= 1

        s = e + 1
        e = min(s + size - 1, n - 1)


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6]]
    k = [3, 5, 1]

    for a_, k_ in zip(a, k):
        reverse_arr(a_, k_)
        print(a_)
