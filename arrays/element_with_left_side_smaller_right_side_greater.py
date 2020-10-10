# https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/

from typing import List


def left_small_right_large(arr: List):
    n = len(arr)
    left_lar = [-1]*n
    right_small = [-1]*n

    m = arr[0]
    for idx in range(1, n):
        left_lar[idx] = m
        m = max(m, arr[idx])
    print(left_lar)

    m = arr[n-1]
    for idx in range(n-2, -1, -1):
        right_small[idx] = m
        m = min(m, arr[idx])
    print(right_small)

    for idx in range(n):
        if idx == 0 and arr[idx] < right_small[idx]:
            return idx
        elif idx == n-1 and arr[idx] > left_lar[idx]:
            return idx
        elif left_lar[idx] < arr[idx] < right_small[idx]:
            return idx

    return -1


if __name__ == "__main__":
    a = [[5, 1, 4, 3, 6, 8, 10, 7, 9], [5, 1, 4, 4]]

    for a_ in a:
        print(left_small_right_large(a_))
