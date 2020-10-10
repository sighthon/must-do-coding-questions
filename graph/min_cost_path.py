# https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/

from typing import List


def min_cost_path(mat: List[List]):
    m = len(mat)
    n = len(mat[0])
    cost_mat = [[(10**10, -1, -1)]*n for _ in range(m)]
    cost_mat[0][0] = (0, -1, -1)

    # idea is Dijikshtra but try to solve using priority queue


if __name__ == "__main__":
    a = [
        [[31, 100, 65, 12, 18],
         [10, 13, 47, 157, 6],
         [100, 113, 174, 11, 33],
         [88, 124, 41, 20, 140],
         [99, 32, 111, 41, 20]]
    ]

    for a_ in a:
        print(min_cost_path(a_))
