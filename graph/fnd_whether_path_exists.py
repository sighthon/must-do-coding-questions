# https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/

from typing import List


def does_path_exist(mat: List[List]):
    src = des = None
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                src = (i, j)
            if mat[i][j] == 2:
                des = (i, j)

    assert src is not None
    assert des is not None

    stack = [src]
    visited = [[False]*n for _ in range(m)]
    visited[src[0]][src[1]] = True
    while stack:
        x, y = stack.pop()
        if x == des[0] and y == des[1]:
            return True

        # add possible paths to explore
        for i, j in zip([x, x, x-1, x+1], [y-1, y+1, y, y]):
            if not 0 <= i < m or not 0 <= j < n:
                continue
            elif not visited[i][j] and mat[i][j] in [0, 2]:
                stack.append((i, j))
                visited[i][j] = True

    return False


if __name__ == "__main__":
    a = [
        [[0, 3, 2],
         [3, 3, 0],
         [1, 3, 0]],
        [[0, 3, 2],
         [3, 3, 0],
         [1, 0, 0]],
    ]

    for a_ in a:
        print(does_path_exist(a_))
