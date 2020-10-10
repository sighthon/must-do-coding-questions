# https://www.geeksforgeeks.org/count-triplets-such-that-one-of-the-numbers-can-be-written-as-sum-of-the-other-two/

from typing import List
from collections import Counter


def nC3(n: int):
    assert n >= 3
    return (n * (n-1) * (n-2)) // 6


def nC2(n: int):
    assert n >= 2
    return (n * (n-1)) // 2


def count_triplets(arr: List):
    # count the occurences
    map_ = Counter(arr)

    ans = 0
    # (0,0,0) case
    if 0 in map_ and map_[0] >= 3:
        ans += nC3(map_[0])

    # (0,x,x) case
    if 0 in map_:
        cnt_0 = map_[0]
        for ele, val in map_.items():
            if ele != 0 and val >= 2:
                ans += cnt_0 * nC2(val)

    # (x, x, 2x) case
    for ele, val in map_.items():
        if val >= 2:
            ans += nC2(val) * map_.get(2*ele, 0)

    # (y, x, x + y) case
    eles = list(map_.keys())
    if len(eles) >= 3:
        for idx in range(len(eles)):
            for idx2 in range(idx+1, len(eles)):
                ans += map_[eles[idx]] * map_[eles[idx2]] * map_.get(eles[idx]+eles[idx2], 0)

    return ans


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5], [1, 1, 1, 2, 2]]
    for a_ in a:
        ans_ = count_triplets(a_)
        print(ans_)
