# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

from typing import List, Dict

# this function is for one node


def detect_cycle_undirected_graph_util(node: int, visited: List, parent: int, adj_list: Dict):
    visited[node] = True

    for child in adj_list[node]:
        if not visited[child]:
            if detect_cycle_undirected_graph_util(child, visited, node, adj_list):
                return True
        elif child != parent:
            return True

    return False


def detect_cycle_undirected_graph(n: int, adj_list: Dict):
    # dfs each node, if we reach a visited node,
    # then cycle

    visited = [False] * n
    for idx in range(n):
        if visited[idx]:
            continue
        if detect_cycle_undirected_graph_util(idx, visited, -1, adj_list):
            return True

    return False


if __name__ == "__main__":
    a = [
        4,
        4
    ]
    e = [
        {0:[1,2], 1:[0,2], 2:[0,1,3], 3:[2]},
        {0: [2], 1:[2], 2:[0, 1, 3], 3:[2]}
    ]

    for a_, e_ in zip(a, e):
        print(detect_cycle_undirected_graph(a_, e_))
