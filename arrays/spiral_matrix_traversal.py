# Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

from typing import List


def spiral_matrix_traversal(matrix: List[List], ans: List, s_r: int, e_r: int, s_c: int, e_c: int):

    if s_r > e_r or s_c > e_c:
        return

    # print(s_r, e_r, s_c, e_c)

    # first row
    for idx in range(s_c, e_c):
        ans.append(matrix[s_r][idx])
    
    # print(ans)

    # last coln
    for idx in range(s_r, e_r):
        ans.append(matrix[idx][e_c])

    # print(ans)

    # last row
    if s_r != e_r:
        for idx in range(e_c, s_c, -1):
            ans.append(matrix[e_r][idx])

    # print(ans)

    # first coln
    if s_c != e_c:
        for idx in range(e_r, s_r, -1):
            ans.append(matrix[idx][s_c])

    # print(ans)

    spiral_matrix_traversal(matrix, ans, s_r+1, e_r-1, s_c+1, e_c-1)


if __name__ == "__main__":
    a = [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
    [[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18]]]

    for a_ in a:
        ans = []
        m = len(a_)
        n = len(a_[0])
        spiral_matrix_traversal(a_, ans, 0, m-1, 0, n-1)
        print(ans)
