# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from typing import List

def dfs(n: int, adj_list: List):
    visited = [False]*n
    ans = []

    for idx in range(n):
        if visited[idx]:
            continue

        stack = [idx]
        visited[idx] = True
        while stack:
            ele = stack.pop()
            ans.append(ele)

            for child in adj_list[ele]:
                if not visited[child]:
                    stack.append(child)
                    visited[child] = True

    return ans

if __name__ == "__main__":
    a = [4]
    e = [{0:[1,2], 1:[2], 2:[0], 3:[3]}]

    for a_, e_ in zip(a, e):
        print(dfs(a_, e_))