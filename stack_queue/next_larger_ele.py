# https://www.geeksforgeeks.org/next-greater-element/

from typing import List


def next_larger(arr: List):
    n = len(arr)
    stack = [0]
    next_larger = [None]*n

    for idx in range(1, n):
        ele = arr[idx]
        if not stack or ele <= arr[stack[-1]]:
            stack.append(idx)
        else:
            while stack and ele > arr[stack[-1]]:
                popped = stack.pop()
                next_larger[popped] = idx

    next_larger = [arr[i] if i else -1 for i in next_larger]
    return next_larger


if __name__ == "__main__":
    a = [[4, 5, 2, 25], [13, 7, 6, 12], [13, 12, 11, 9]]

    for a_ in a:
        print(next_larger(a_))
