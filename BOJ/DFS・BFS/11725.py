# 11725 : 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, graph, parent):
    for i in graph[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, graph, parent)


dfs(1, graph, parent)

for p in parent[2:]:
    print(p)