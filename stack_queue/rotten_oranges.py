# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/

from typing import List


def min_time_to_rot(mat: List[List]):
    m = len(mat)
    n = len(mat[0])

    rotten = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 2:
                rotten.append((i, j, 0))
    rotten.append((-1, -1, -1))  # delimiter

    # number of bfs levels needed
    ans = 0
    visited = [[False]*n for _ in range(m)]
    while rotten:
        x, y, lev = rotten.pop(0)
        if x == -1 and y == -1:
            if not rotten:
                break
            rotten.append((-1, -1, -1))
            continue

        # run 1 level bfs for popped node
        for ii, jj in zip([x, x, x-1, x+1], [y-1, y+1, y, y]):
            if not 0 <= ii < m or not 0 <= jj < n:
                continue
            elif not visited[ii][jj] and mat[ii][jj] == 1:
                rotten.append((ii, jj, lev+1))
                mat[ii][jj] = 2
                visited[ii][jj] = True

        ans = max(ans, lev)

    return ans


if __name__ == "__main__":
    a = [
        [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]],
        [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 1, 0, 2, 1]]
    ]

    for a_ in a:
        print(min_time_to_rot(a_))
