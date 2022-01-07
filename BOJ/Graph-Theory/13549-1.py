# 13549 : 숨바꼭질 3 - dijkstra

import sys
import heapq
INF = int(1e9)
n, k = map(int, sys.stdin.readline().split())
end = 100001
distance = [INF for _ in range(end)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == k:
            break

        for x in ((0, 2*now), (1, now-1), (1, now+1)):
            cost = dist + x[0]
            if 0 <= x[1] < end and cost < distance[x[1]]:
                distance[x[1]] = cost
                heapq.heappush(q, (cost, x[1]))


if k <= n:
    print(n-k)
else:
    dijkstra(n)
    print(distance[k])