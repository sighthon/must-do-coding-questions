# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

from typing import List


def min_swaps(arr: List):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda x: x[1])
    print(arrpos)

    visited = [False]*n
    ans = 0
    for idx in range(n):
        if visited[idx] or arrpos[idx][0] == idx:
            continue

        # find cycle length
        cycle_len = 0
        j = idx
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0]
            cycle_len += 1
        ans += (cycle_len-1)

    return ans


if __name__ == "__main__":
    a = [[4, 3, 2, 1], [1, 5, 4, 3, 2]]

    for a_ in a:
        print(min_swaps(a_))
