# 1865 : 웜홀

import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
        for i in range(1, N+1):
            for j in range(1, N+1):
                for next_node, cost in edges[j]:
                    if dist[next_node] > dist[j]+cost:
                        dist[next_node] = dist[j]+cost
                        if i == N:
                            return True
        return False

t = int(input())
for _ in range(t):
    N, M, W = map(int, input().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges[S].append((E, T))
        edges[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges[S].append((E, -T))

    dist = [INF] * (N+1)
    cycle = bf(1)

    if cycle == True:
        print("YES")
    else:
        print("NO")