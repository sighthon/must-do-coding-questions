# https://www.geeksforgeeks.org/write-your-own-atoi/

from typing import List


def implement_atoi(s: str):
    ans = 0
    for idx in range(len(s)):
        ans = ans*10 + (ord(s[idx]) - ord('0'))

    return ans

if __name__ == "__main__":
    a = ["12546"]

    for a_ in a:
        print(implement_atoi(a_))