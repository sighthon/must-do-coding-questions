# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

from typing import List, Dict
from collections import defaultdict

# this function is for one node


def detect_cycle_directed_graph_util(node: int, visited: List, adj_list: Dict, rec_stack: List):
    visited[node] = True
    rec_stack[node] = True

    for child in adj_list[node]:
        if not visited[child]:
            if detect_cycle_directed_graph_util(child, visited, adj_list, rec_stack):
                return True
        elif rec_stack[child]:
            return True

    rec_stack[node] = False
    return False


def detect_cycle_directed_graph(n: int, adj_list: Dict):
    # dfs each node, if we reach a visited node,
    # then cycle

    visited = [False] * n
    rec_stack = [False] * n
    for idx in range(n):
        if visited[idx]:
            continue
        if detect_cycle_directed_graph_util(idx, visited, adj_list, rec_stack):
            return True

    return False


if __name__ == "__main__":
    a = [
        4,
        4
    ]
    e = [
        defaultdict(lambda : [], {0:[1,2], 1:[2], 2:[0,3], 3:[3]}),
        defaultdict(lambda : [], {0: [1, 2], 1:[2], 2:[3]})
    ]

    for a_, e_ in zip(a, e):
        print(detect_cycle_directed_graph(a_, e_))
