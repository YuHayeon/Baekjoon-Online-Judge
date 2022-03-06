# 15686 : 치킨 배달

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
chicken, home = [], {}
choose = []
result = []


def choose_chicken(start, chicken, M):
    if len(choose) == M:
        return chicken_distance(choose)

    for i in range(start, len(chicken)):
        if len(choose) == M:
            break

        choose.append(chicken[i])
        choose_chicken(i+1, chicken, M)
        choose.pop()


def chicken_distance(choose):
    for hx, hy in home.keys():
        home[(hx, hy)] = INF
        for cx, cy in choose:
            home[(hx, hy)] = min(home[(hx, hy)], abs(cx-hx) + abs(cy-hy))

    return result.append(sum(home.values()))


for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            home[(i, j)] = 0

choose_chicken(0, chicken, M)
print(min(result))