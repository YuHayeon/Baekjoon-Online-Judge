# 1260 : DFS와 BFS

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for i in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    visited1[v] = 1
    print(v, end=' ')

    for i in range(1, n+1):
        if visited1[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited2[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if visited2[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                visited2[i] = 1


dfs(v)
print()
bfs(v)