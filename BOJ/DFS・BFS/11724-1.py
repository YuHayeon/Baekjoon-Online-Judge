# 11724 : 연결 요소의 개수 - DFS

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        # 
        if visited[i] == 0:
            dfs(i)


for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)