# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

from typing import List, Dict
from collections import defaultdict


def top_sort_util(node: str, adj_list: Dict, visited: Dict, ans: List):
    visited[node] = True

    for child in adj_list.get(node, []):
        if not visited.get(child, False):
            top_sort_util(child, adj_list, visited, ans)
    ans.insert(0, node)


def alien_dict(arr: List):
    n = len(arr)

    # create a directed graph of characters
    adj_list = defaultdict(lambda: [])
    for idx in range(1, n):
        # compare 2 consecutive words
        w1 = arr[idx-1]
        w2 = arr[idx]
        i = j = 0
        while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
            i += 1
            j += 1

        if i < len(w1) and j < len(w2):
            adj_list[w1[i]].append(w2[j])

    # topological sort of adj list
    ans = []
    visited = {k: False for k in adj_list.keys()}
    for node in adj_list.keys():
        if not visited.get(node, False):
            top_sort_util(node, adj_list, visited, ans)

    return ans


if __name__ == "__main__":
    a = [["baa", "abcd", "abca", "cab", "cad"], ["caa", "aaa", "aab"]]

    for a_ in a:
        print(alien_dict(a_))
