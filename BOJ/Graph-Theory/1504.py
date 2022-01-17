# 1504 : 특정한 최단 경로

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

result = -1

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return distance[end]

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return INF

v = dijkstra(v1, v2)
dist1 = dijkstra(1, v1)+v+dijkstra(v2, N)
dist2 = dijkstra(1, v2)+v+dijkstra(v1, N)

result = min(dist1, dist2)

print(-1 if result>=INF else result)