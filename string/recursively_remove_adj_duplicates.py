# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

from typing import List
import sys


def remove_adj_duplicates(s: List, idx: int):
    if not 0 <= idx < len(s):
        return s

    if idx == 0 or s[idx] != s[idx-1]:
        s = remove_adj_duplicates(s, idx+1)
    else:
        s_idx = idx-1
        while idx < len(s) and s[idx] == s[idx-1]:
            idx += 1
        idx -= 1
        s = s[:s_idx] + s[idx+1:]
        s = remove_adj_duplicates(s, s_idx)

    return s


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    a = ["geeksforgeeg", "azxxzy", "caaabbbaacdddd", "acaaabbbacdddd", "aabbccdd"]
    for a_ in a:
        b = list(a_)
        b = remove_adj_duplicates(b, 0)
        print(b)
