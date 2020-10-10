# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from typing import List

def bfs(n: int, adj_list: List):
    visited = [False]*n
    ans = []

    for idx in range(n):
        if visited[idx]:
            continue

        queue = [idx]
        visited[idx] = True
        while queue:
            ele = queue.pop(0)
            ans.append(ele)

            for child in adj_list[ele]:
                if not visited[ele]:
                    queue.append(child)
                    visited[ele] = True

    return ans

if __name__ == "__main__":
    a = [4]
    e = [{0:[1,2], 1:[2], 2:[0,3], 3:[3]}]

    for a_, e_ in zip(a, e):
        print(bfs(a_, e_))