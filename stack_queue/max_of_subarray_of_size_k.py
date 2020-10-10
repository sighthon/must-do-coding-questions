# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# sliding window, use deque

from typing import List
from collections import deque


def max_subarr_size_k(arr: List, k: int):
    n = len(arr)
    ans = []
    Q = deque()
    for i in range(k):
        # remove all smaller elements
        while Q and arr[i] > arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k, n):
        print(Q)
        ans.append(arr[Q[0]])

        # remove out of the window ele
        while Q and Q[0] <= i - k:
            Q.popleft()

        # remove smaller ones
        while Q and arr[i] > arr[Q[-1]]:
            Q.pop()

        Q.append(i)
    ans.append(arr[Q[0]])
    return ans

if __name__ == "__main__":
    a = [[1, 2, 3, 1, 4, 5, 2, 3, 6]]
    k = [3]

    for a_, k_ in zip(a, k):
        print(max_subarr_size_k(a_, k_))
