# https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/

from typing import List


def remove_duplicates(s: str):
    ans = ""
    found = []

    for ch in s:
        if ch.lower() in found:
            continue
        else:
            ans += ch
            found.append(ch.lower())

    return ans

if __name__ == "__main__":
    a = ["geeksforGeeks", "gfg"]

    for a_ in a:
        print(remove_duplicates(a_))
