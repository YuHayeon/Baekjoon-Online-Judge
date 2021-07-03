# 9-2 : 미래 도시

import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())

graph = [[inf] * (n+1) for _ in range (n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    for a in range(1,n+1):
        for b in range (1,n+1):
            if graph[a][i] + graph[i][b] < graph[a][b]:
                graph[a][b] = graph[a][i] + graph[i][b]

result = graph[1][k] + graph[k][x]
if result < inf:
    print(result)
else:
    print("-1")