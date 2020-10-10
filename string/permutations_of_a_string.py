# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

from typing import List
import sys


def string_permutations(s: List, ans: List, st: int, en: int):

    if st == en:
        ans.append("".join(s))
        return

    for i in range(st, en+1):
        s[st], s[i] = s[i], s[st]
        string_permutations(s, ans, st+1, en)
        s[st], s[en] = s[en], s[st]


if __name__ == "__main__":
    a = ["ABC", "ABCD"]
    sys.setrecursionlimit(5000)
    for a_ in a:
        ans = []
        string_permutations(list(a_), ans, 0, len(a_)-1)
        print(ans)
