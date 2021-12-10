# 1992 : 쿼드 트리

import sys

n = int(sys.stdin.readline())
d = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

def quad(n, r, c):
    target = d[r][c]
    cnt = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            if target != d[i][j]:
                print("(", end='')
                quad(n//2, r, c)
                quad(n//2, r, c+n//2)
                quad(n//2, r+n//2, c)
                quad(n//2, r+n//2, c+n//2)
                print(")", end='')
                return

    if target==0:
        print("0", end='')
    elif target==1:
        print("1", end='')     


quad(n, 0, 0)