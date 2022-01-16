# 1167 : 트리의 지름

# 임의의 정점에서 dfs로 가장 먼 정점을 찾음
# 찾은 정점에서 dfs로 다시 가장 먼 정점을 찾으면
# 그 거리가 트리의 지름이 됨

import sys
input = sys.stdin.readline


def dfs(n, result):
    for next_node, cost in tree[n]:
        if dist[next_node] == -1:
            dist[next_node] = result+cost
            dfs(next_node, result+cost)


V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    e = list(map(int, input().split()))
    for i in range(1, len(e)-1, 2):
        tree[e[0]].append((e[i], e[i+1]))

dist = [-1] * (V+1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1] * (V+1)
dist[start] = 0
dfs(start, 0)

print(max(dist))