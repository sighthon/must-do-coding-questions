# https://www.geeksforgeeks.org/find-number-of-pairs-x-y-in-an-array-such-that-xy-yx-set-2/

from typing import List


def num_of_pairs(arr_a: List, arr_b: List):
    # Many corner cases
    pass


if __name__ == "__main__":
    a = [[2, 1, 6]]
    b = [[1, 5]]

    for a_, b_ in zip(a, b):
        print(num_of_pairs(a_, b_))
