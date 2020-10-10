# https://practice.geeksforgeeks.org/problems/last-index-of-1/0

from typing import List


def last_idx_1(s: str):
    ans = -1
    for idx, ch in enumerate(s):
        if ch == "1":
            ans = idx
    return ans


if __name__ == "__main__":
    a = ["00001", "0"]

    for a_ in a:
        print(last_idx_1(a_))
