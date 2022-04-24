# 1939 : 중량제한

from collections import deque
import sys
input = sys.stdin.readline

# 중량 이진탐색으로 최댓값을 찾음
def binary_search(weight_set):
    #중량을 저장한 집합을 리스트 형태로 바꿔줌
    weight_list = list(weight_set)
    weight_list.sort()

    left, right = 0, len(weight_list)-1
    result = 0

    while left <= right:
        mid = (left+right) // 2
        if bfs(weight_list[mid]):
            result = weight_list[mid]
            left = mid+1
        else:
            right = mid-1
    return result


# 이진탐색으로 선택한 중량이 가능한지 확인
def bfs(target):
    q = deque()
    q.append(start)
    visited = [False for _ in range(N+1)]
    visited[start] = 1

    while q:
        now = q.popleft()
        # 끝 노드에 도착한다면 True
        if end == now:
            return True

        for x, w in graph[now]:
            # 방문하지 않았고 선택한 중량이 중량제한에 걸리지 않는다면
            if not visited[x] and target <= w:
                visited[x] = 1
                q.append(x)

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
weight_set = set()

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    weight_set.add(C)

start, end = map(int, input().split())

print(binary_search(weight_set))