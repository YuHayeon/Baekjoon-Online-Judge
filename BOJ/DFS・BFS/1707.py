# 1707 : 이분 그래프 - BFS

import sys
from collections import deque

# 테스트 케이스 수 입력
t = int(sys.stdin.readline())
for _ in range(t):
    # 정점과 간선 정보 입력
    v, e = map(int, sys.stdin.readline().split())
    # 빈 그래프 생성
    graph = [[] for _ in range(v+1)]
    # 방문했는지 여부 체크하는 그래프 생성
    visited = [0] * (v+1)
    
    # 입력받은 연결 정보를 무방향 그래프에 저장
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(v, graph):
        # 1에서부터만 확인하면 안됨. 전체적으로 탐색해야하기 때문에 1부터 정점 끝까지 모두 탐색
        for i in range(1, v+1):
            # 노드에 방문하지 않았다면
            if visited[i] == 0:
                # 큐에 저장하고 visited = 1 방문 표시
                q = deque()
                q.append(i)
                visited[i] = 1

                while q:
                    v = q.popleft()
                    # 현재 노드와 연결된 노드 확인하기
                    for w in graph[v]:
                        # 연결된 노드를 방문하지 않았다면
                        if visited[w] == 0:
                            # 큐에 append
                            q.append(w)
                            # 현재 값에 -1를 곱해 다른 색깔이라고 가정.
                            visited[w] = visited[v] * -1
                            # 만약 현재 노드와 연결된 노드가 같은 색깔이라면
                        elif visited[w] == visited[v]:
                            # 이분 그래프가 아니므로 False 반환
                            return False
        return True

    if bfs(v, graph) == True:
        print("YES")
    else:
        print("NO")