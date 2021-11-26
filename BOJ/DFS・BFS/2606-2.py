# 2606 : 바이러스 - BFS

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
result = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for i in range(1, n+1):
            if visited[i] == 0 and matrix[v][i] ==1:
                queue.append(i)
                visited[i] = 1
        

bfs(1)
ans = sum(visited)-1
print(ans)