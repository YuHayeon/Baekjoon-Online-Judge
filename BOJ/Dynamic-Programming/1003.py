# 1003 : 피보나치 함수

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    d = [[1, 0], [0, 1]] + [[0]*2 for _ in range(n-1)]

    for i in range(2, n+1):
        d[i] = [d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]

    print(d[n][0], d[n][1])
