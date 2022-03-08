# 2583 : 영역 구하기

import sys
from collections import deque
input = sys.stdin.readline
area = 0
result = []


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = dx+x
            ny = dy+y

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))

    return cnt


M, N, K = map(int, input().split())
graph = [[1 for _ in range(N)] for _ in range(M)]
square = []

for _ in range(K):
    square.append(tuple(map(int, input().split())))

# 직사각형 내부를 1->0으로 변경하기
for y1, x1, y2, x2 in square:
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 0

# bfs실행하면서 직사각형을 제외한 나머지 부분 개수 세기
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
            area += 1

result.sort()

print(area)
print(*result)