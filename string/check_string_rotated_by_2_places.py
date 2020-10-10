# https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/

from typing import List


def check(s1: str, s2: str):
    return s1 == s2[2:] + s2[:2] or s1 == s2[-2:] + s2[:-2]

if __name__ == "__main__":
    a = ["amazon", "amazon"]
    b = ["azonam", "onamaz"]

    for a_, b_ in zip(a, b):
        print(check(a_, b_))
