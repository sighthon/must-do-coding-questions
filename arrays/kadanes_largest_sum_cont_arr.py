# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# KADANE's algo

from typing import List
import sys
MAX_INT = sys.maxsize - 1


def get_max_sum(arr: List):
    if not arr:
        return 0

    n = len(arr)
    max_ending_here = 0
    max_so_far = -MAX_INT

    for ele in arr:
        max_ending_here += ele

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


if __name__ == "__main__":
    a = [[-2, -3, 4, -1, -2, 1, 5, -3]]
    for a_ in a:
        ans_ = get_max_sum(a_)
        print(ans_)
