# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

from typing import List


def reverse_words(s: str):
    rev_str = list(reversed(list(s)))
    space_idxs = [i for i in range(len(rev_str)) if rev_str[i] == " "]
    space_idxs.insert(0, -1)
    space_idxs.append(len(s))

    for idx in range(1, len(space_idxs)):
        s = space_idxs[idx-1]
        e = space_idxs[idx]
        rev_str = rev_str[:s+1] + list(reversed(rev_str[s+1:e])) + rev_str[e:]

    return "".join(rev_str)

if __name__ == "__main__":
    a = ["i'm love programming very much"]

    for a_ in a:
        print(reverse_words(a_))
