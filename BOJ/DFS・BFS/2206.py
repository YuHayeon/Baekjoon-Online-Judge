# 2206 : 벽 부수고 이동하기

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    # queue를 만들고 [0,0]에서 시작. [0,0]는 방문했기 때문에 visited[0][0][0]은 1로 변경
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1

    while q:
        x, y, z = q.popleft()

        # 상하좌우로 이동
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 만약 한번도 방문하지 않고 graph에서 0이라면 q에 넣고 이전 경로에서 +1를 visited에 저장
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                q.append((nx, ny, z))
                visited[nx][ny][z] = 1+visited[x][y][z]

            # 한번도 방문하지 않고 graph에서 1일 경우 
            if graph[nx][ny] == 1 and visited[nx][ny][z] == 0 and z == 0:
                # 벽을 부순 상태인 visited[x][y][1]에 저장
                q.append((nx, ny, 1))
                visited[nx][ny][1] = 1+visited[x][y][z]


bfs(0, 0, 0)
ans1, ans2 = visited[n-1][m-1][0], visited[n-1][m-1][1]
if ans1 == 0 and ans2 == 0:
    print(-1)
elif ans1 == 0:
    print(ans2)
elif ans2 == 0:
    print(ans1)
else:
    print(min(ans1, ans2))