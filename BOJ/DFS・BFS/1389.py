# 1389 : 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    dist = [0]*(N+1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[x]+1
                q.append(i)

    return sum(dist)


result = [int(1e9)]
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    result.append(bfs(i))

print(result.index(min(result)))