# 1647 : 도시 분할 계획

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [i for i in range(0, N+1)]
graph = []
result = 0
select = []


for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

for i in graph:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        select.append(cost)
        result += cost

result -= select[-1]

print(result)