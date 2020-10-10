# https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/

from typing import List


def shortest_path(mat: List[List], src_x: int, src_y: int, des_x: int, des_y: int):
    m= len(mat)
    n= len(mat[0])

    distances= [[10*10]*n for _ in range(m)]
    visited= [[False]*n for _ in range(m)]

    distances[src_x][src_y]= 0
    visited[src_x][src_y]= True

    # bfs starting from source
    queue= [(src_x, src_y)]
    while queue:
        node_x, node_y= queue.pop(0)
        if node_x == des_x and node_y == des_y:
            for i in range(m):
                for j in range(n):
                    print(distances[i][j], end=" ")
                print()
            return distances[node_x][node_y]

        # update child distances
        for i, j in zip([node_x, node_x, node_x-1, node_x+1], [node_y-1, node_y+1,node_y, node_y]):
            # print(i, j)
            if not 0 <= i < m or not 0 <= j < n:
                continue
            if mat[i][j] and not visited[i][j]:
                distances[i][j]= min(distances[i][j], distances[node_x][node_y]+1)
                visited[i][j]= True
                queue.append((i, j))
    
    for i in range(m):
        for j in range(n):
            print(distances[i][j], end=" ")
        print()
    return -1



if __name__ == "__main__":
    a= [
        [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    ]

    for a_ in a:
        print(shortest_path(a_, 0, 0, 8, 9))
