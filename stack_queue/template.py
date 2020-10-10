# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

from typing import List


def is_balanced(s: str):
    # push and pop from stack
    map_ = {"}": "{", "]": "[", ")": "("}
    idx = 0
    stack = []
    while idx < len(s):
        if not stack or s[idx] in ["{", "[", "("]:
            stack.append(s[idx])
        elif stack[-1] == map_.get(s[idx], ""):
            stack.pop()
        idx += 1

    return len(stack) == 0

if __name__ == "__main__":
    a = ["[()]{}{[()()]()}", "[(])"]

    for a_ in a:
        print(is_balanced(a_))
