# 2630 : 색종이 만들기

import sys

n = int(sys.stdin.readline())
d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue = 0
white = 0


def paper(n, r, c):
    global blue
    global white
    cnt = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            if d[i][j] == 1:
                cnt += 1
    if cnt == 0:
        white += 1
    elif cnt == (n**2):
        blue += 1
    else:
        # for x in range(2):
        #     for y in range(2):
        #         paper(n//2, r+(n//2*x), c+(n//2*y))
        paper(n//2, r, c)
        paper(n//2, r+n//2, c)
        paper(n//2, r, c+n//2)
        paper(n//2, r+n//2, c+n//2)


paper(n, 0, 0)
print(white)
print(blue)
