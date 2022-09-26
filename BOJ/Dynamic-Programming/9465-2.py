# 9465 : 스티커

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    d = [[0 for _ in range(n)] for _ in range(2)]

    d[0][0], d[1][0] = stickers[0][0], stickers[1][0]
    if n > 1:
        d[0][1], d[1][1] = stickers[1][0]+stickers[0][1], stickers[0][0]+stickers[1][1]

        for i in range(2, n):
            d[0][i] = max(d[1][i-1], d[1][i-2])+stickers[0][i]
            d[1][i] = max(d[0][i-1], d[0][i-2])+stickers[1][i]

    answer = max(d[0][-1], d[1][-1])

    print(answer)
