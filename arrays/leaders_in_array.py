# https://www.geeksforgeeks.org/leaders-in-an-array/

from typing import List


def leaders(arr: List):
    n = len(arr)

    leaders = [arr[-1]]
    max_ = arr[-1]
    for idx in range(n-2, -1, -1):
        if arr[idx] > max_:
            leaders.insert(0, arr[idx])
            max_ = arr[idx]

    return leaders


if __name__ == "__main__":
    a = [[16, 17, 4, 3, 5, 2]]

    for a_ in a:
        print(leaders(a_))