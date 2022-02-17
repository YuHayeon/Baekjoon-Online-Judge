from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
wall_list = []
result = 0

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y, lab):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]

            if 0 <= nx < n and 0 <= ny < m:
                if lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    q.append((nx, ny))


def wall(wall_cnt):
    global result

    if wall_cnt == 3:
        lab = [x[:] for x in graph]  # 깊은 복사
        cnt = 0

        for i in range(n):
            for j in range(m):
                if lab[i][j] == 2:
                    bfs(i, j, lab)

        for i in lab:
            for j in i:
                if j == 0:
                    cnt += 1

        result = max(result, cnt)
        return

    for i in range(n):
        for j in range(m):

            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(wall_cnt + 1)
                graph[i][j] = 0


wall(0, 0, 0)

print(result)