# https://practice.geeksforgeeks.org/problems/implement-strstr/1

from typing import List


def implement_strstr(s: str, x: str):
    m = len(s)
    n = len(x)

    for i in range(m-n+1):
        j = 0
        while j < n:
            if s[i+j] != x[j]:
                break
            j += 1

        if j == n:
            return i

    return -1


if __name__ == "__main__":
    a = ["GeeksForGeeks", "GeeksForGeeks"]
    b = ["For", "Fr"]

    for a_, b_ in zip(a, b):
        print(implement_strstr(a_, b_))
