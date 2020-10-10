# https://www.geeksforgeeks.org/trapping-rain-water/

from typing import List


def trapping_rain_water(arr: List):
    n = len(arr)
    max_left = [0] * n
    max_right = [0] * n

    m = arr[0]
    for idx in range(1, n):
        max_left[idx] = m
        m = max(m, arr[idx])

    m = arr[n-1]
    for idx in range(n-2, -1, -1):
        max_right[idx] = m
        m = max(m, arr[idx])

    print(max_left)
    print(max_right)

    ans = 0
    for idx in range(n):
        if min(max_left[idx], max_right[idx]) > arr[idx]:
            ans += min(max_left[idx], max_right[idx]) - arr[idx]

    return ans


if __name__ == "__main__":
    a = [[2, 0, 2], [3, 0, 2, 0, 4], [3, 0, 5, 0, 3], [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]

    for a_ in a:
        print(trapping_rain_water(a_))