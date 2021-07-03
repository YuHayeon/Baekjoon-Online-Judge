# 9-3 : 전보

import sys
import heapq
from math import inf

n, m, c = map(int, sys.stdin.readline().split())

graph = [[] * (n+1) for _ in range (n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y,x))

def dijkstra(c):
    q=[]
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance [i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(c)

count = 0
max_dist = 0
for i in distance:
    if i != inf:
        count += 1
        max_dist = max(max_dist, i)
print(distance)
print(count-1, max_dist)

