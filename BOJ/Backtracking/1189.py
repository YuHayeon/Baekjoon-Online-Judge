# 1189 : 컴백홈

import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
maps = [list(map(str, input().strip())) for _ in range(r)]
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
way = [(r-1, 0)]
visited = [[False for _ in range(c)] for _ in range(r)]
visited[r-1][0] = True
count = 0

def dfs(way, visited):
    global count
    if len(way) == k and way[-1] == ((0, c-1)):
        print(way)
        count += 1
        return

    for i in range(4):
        nx = way[-1][0]+d[i][0]
        ny = way[-1][1]+d[i][1]

        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == '.' and visited[nx][ny] == False:
            way.append((nx, ny))
            visited[nx][ny] = True
            dfs(way, visited)
            way.pop()
            visited[nx][ny] = False

dfs(way, visited)
print(count)
