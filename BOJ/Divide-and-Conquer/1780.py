# 1780 : 종이의 개수

import sys

n = int(sys.stdin.readline())
d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
one = 0
zero = 0
minus = 0

def paper(n, r, c):
    global one
    global zero
    global minus
    target = d[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if d[i][j] != target:
                # for x in range(3):
                #     for y in range(3):
                #         paper(n//3, r+(n//3 * x), c+(n//3* y))
                paper(n//3, r, c)
                paper(n//3, r, c+n//3)
                paper(n//3, r, c+2*(n//3))
                paper(n//3, r+n//3, c)
                paper(n//3, r+n//3, c+n//3)
                paper(n//3, r+n//3, c+2*(n//3))
                paper(n//3, r+2*(n//3), c)
                paper(n//3, r+2*(n//3), c+n//3)
                paper(n//3, r+2*(n//3), c+2*(n//3))
                return

    if target == 0:
        zero += 1
    elif target == -1:
        minus += 1
    elif target == 1:
        one += 1

paper(n, 0, 0)        
print(minus)
print(zero)
print(one)