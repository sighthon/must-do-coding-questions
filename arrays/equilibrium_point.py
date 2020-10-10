# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

from typing import List


def equilibrium_idx(arr: List):
    if not arr:
        return

    n = len(arr)
    sum_a = [0]*n

    sum_a[0] = arr[0]
    for i in range(1, n):
        sum_a[i] = sum_a[i-1] + arr[i]

    sum_b = arr[-1]
    for i in range(n-2, -1, -1):
        sum_b += arr[i]
        if sum_b == sum_a[i]:
            return i

    return -1


if __name__ == "__main__":
    a = [[-7, 1, 5, 2, -4, 3, 0], [1, 2, 3], [0, 0, 1, 0]]

    for a_ in a:
        print(equilibrium_idx(a_))
