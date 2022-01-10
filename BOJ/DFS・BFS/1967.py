# 1967 : 트리의 지름

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
result = 0

for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])


def dfs(start):
    global result
    now_max, max_dist = 0, 0
    for i in tree[start]:
        # 현재 노드와 연결된 노드 중 가장 긴 길이 + 현재 길이
        r = dfs(i[0]) + i[1]
        # 현재 노드를 기준으로 깊이 들어갔을 때 가장 긴 길이
        max_dist = max(max_dist, now_max+r)
        # 현재 노드와 연결된 노드를 기준으로 가장 긴 길이
        now_max = max(now_max, r)
    result = max(result, max_dist)
    return now_max


dfs(1)
print(result)