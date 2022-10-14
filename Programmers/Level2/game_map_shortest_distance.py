# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# Programmers LEVEL 2 - 게임 맵 최단거리

from collections import deque

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            return visited[n-1][m-1]

        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]+1
    return -1

def solution(maps):
    answer = 0
    answer = bfs(maps)
    return answer
