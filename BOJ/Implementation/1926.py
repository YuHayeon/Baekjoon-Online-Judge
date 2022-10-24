# 1926 : 그림

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(pictures, x, y):
    q = deque()
    q.append((x, y))
    pictures[x][y] = 0
    area = 1

    while q:
        x, y = q.popleft()
        for d in directions:
            nx = x+d[0]
            ny = y+d[1]
            if 0 <= nx < n and 0 <= ny < m and pictures[nx][ny] == 1:
                area += 1
                pictures[nx][ny] = 0
                q.append((nx, ny))

    return area

answer = 0
area = 0
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1:
            area = max(area, bfs(pictures, i, j))
            answer += 1

print(answer)
print(area)
