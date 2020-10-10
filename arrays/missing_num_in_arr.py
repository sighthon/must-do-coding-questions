# https://www.geeksforgeeks.org/find-the-missing-number/

from typing import List


def arr_missing_num(arr: List):
    if not arr:
        return 0

    n = len(arr) + 1
    return ((n*(n+1))//2) - sum(arr)


if __name__ == "__main__":
    a = [[1, 2, 4, 6, 3, 7, 8], [1, 2, 3, 5]]
    for a_ in a:
        ans_ = arr_missing_num(a_)
        print(ans_)
