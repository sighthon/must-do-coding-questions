# https://www.geeksforgeeks.org/topological-sorting/

from typing import List


def top_sort_util(node: int, adj_list: List, visited: List, ans: List):
    visited[node] = True

    for child in adj_list.get(node, []):
        if not visited[child]:
            top_sort_util(child, adj_list, visited, ans)

    ans.insert(0, node)


def top_sort(n: int, adj_list: List):
    visited = [False]*n
    ans = []

    for idx in range(n):
        if visited[idx]:
            continue
        top_sort_util(idx, adj_list, visited, ans)

    return ans


if __name__ == "__main__":
    a = [
        4,
        6
    ]
    e = [
        {0: [1, 2], 1:[2], 2:[3]},
        {0: [], 1:[], 2:[3], 3:[1], 4:[0, 1], 5:[0, 2]}
    ]

    for a_, e_ in zip(a, e):
        print(top_sort(a_, e_))
