# https://www.geeksforgeeks.org/find-number-of-islands/

from typing import List


def mark_visited(mat: List[List], visited: List[List], r: int, c: int, n: int):

    visited[r][c] = True
    for i in [r-1, r, r+1]:
        for j in [c-1, c, c+1]:
            if not 0 <= i < n or not 0 <= j < n:
                continue
            if not visited[i][j] and mat[i][j]:
                mark_visited(mat, visited, i, j, n)


def number_of_islands(mat: List[List]):
    n = len(mat)
    visited = [[False]*n for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            elif mat[i][j]:
                ans += 1
                mark_visited(mat, visited, i, j, n)

    return ans


if __name__ == "__main__":
    a = [
        [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
    ]

    for a_ in a:
        print(number_of_islands(a_))
