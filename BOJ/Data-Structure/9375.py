# 9375 : 패션왕 신해빈

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dict = {}
    cnt = 1

    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in dict:
            dict[kind] += 1
        else:
            dict[kind] = 1

    for v in dict.values():
        cnt *= (v+1)

    print(cnt-1)
