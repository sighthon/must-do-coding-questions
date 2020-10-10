# https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/

from typing import List


def can_form_circle_of_strings(arr: List):
    # create an adj list of directed paths
    n = len(arr)
    adj_list = [[0]*n for _ in range(n)]
    nodes = [(s[0], s[-1]) for s in arr]
    print(nodes)

    for i in range(n):
        for j in range(i, n):
            if nodes[i][1] == nodes[j][0]:
                adj_list[i][j] = 1
            if nodes[j][1] == nodes[i][0]:
                adj_list[j][i] = 1

    for i in range(n):
        for j in range(n):
            print(adj_list[i][j], end=" ")
        print()

    # TODO: The idea is to check for eulerean circuit (SCC)


if __name__ == "__main__":
    a = [["for", "geek", "rig", "kaf"]]

    for a_ in a:
        print(can_form_circle_of_strings(a_))
