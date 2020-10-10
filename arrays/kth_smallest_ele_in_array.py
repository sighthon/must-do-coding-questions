# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
# Quick Select

from typing import List


def partition(arr: List, s: int, e: int):
    pivot = arr[e]
    i = s - 1
    for j in range(s, e):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[e] = arr[e], arr[i+1]
    return i+1


def kth_smallest(arr: List, s: int, e: int, size: int):
    if size > e-s+1:
        return -1

    par = partition(arr, s, e)
    if par-s+1 == size:
        return arr[par]
    elif par-s+1 > size:
        return kth_smallest(arr, s, par-1, size)
    return kth_smallest(arr, par+1, e, size-(par-s+1))


if __name__ == "__main__":
    a = [[7, 10, 4, 3, 20, 15], [7, 10, 4, 3, 20, 15]]
    k = [3, 4]

    for a_, k_ in zip(a, k):
        n = len(a_)
        print(kth_smallest(a_, 0, n-1, k_))
