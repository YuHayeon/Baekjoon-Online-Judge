# 15649 : N과 M (1)

import sys
n, m = map(int,sys.stdin.readline().split())
s = []

def back(n):
    if len(s) == m:
        print(' '.join(map(str,s)))

    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        back(n)
        s.pop()

back(n)

