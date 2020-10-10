# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

from typing import List

def lcp_util(s1: str, s2: str):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            break
        i += 1
        j += 1
    return s1[:i]


def longest_common_prefix(arr: List[str]):
    ans = arr[0]
    for idx in range(1, len(arr)):
        ans = lcp_util(ans, arr[idx])

    return ans

if __name__ == "__main__":
    a = [["geeksforgeeks", "geeks", "geek", "geezer"],
    ["apple", "ape", "april"]]

    for a_ in a:
        print(longest_common_prefix(a_))
