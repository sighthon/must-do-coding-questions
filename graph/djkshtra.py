# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

from typing import List


def dijkshtra(n: int, adj_list: List, source: int):
    vertices_set = set()
    distances = [10**10]*n

    distances[source] = 0

    while len(vertices_set) < n:
        # get the node with min distance and not in set
        min_ = 10**10
        node = None
        for idx in range(len(distances)):
            if distances[idx] < min_ and idx not in vertices_set:
                node = idx

        assert node is not None

        # update neighbours
        vertices_set.add(node)
        for neigh in adj_list.get(node, []):
            distances[neigh] = min(distances[neigh], distances[node]+1)

    return distances


if __name__ == "__main__":
    a = [4]
    e = [{0: [1, 2], 1:[2], 2:[0, 3], 3:[3]}]

    for a_, e_ in zip(a, e):
        print(dijkshtra(a_, e_, 0))