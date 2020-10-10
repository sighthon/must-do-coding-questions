# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

from typing import List


def are_anagrams(s1: str, s2: str):
    return "".join(sorted(list(s1))) == "".join(sorted(list(s2)))

if __name__ == "__main__":
    a = ["geeksforgeeks", "allergy"]
    b = ["forgeeksgeeks", "allergic"]

    for a_, b_ in zip(a,b):
        print(are_anagrams(a_, b_))
