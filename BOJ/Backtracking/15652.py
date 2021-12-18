# 15652 : N과 M (4)

import sys

n, m = map(int, sys.stdin.readline().split())
s=[]

def back(start):
    if len(s) == m:
        print(' '.join(map(str,s)))

    for i in range(start, n+1):
        if len(s)==m:
            continue
        s.append(i)
        back(i)
        s.pop()

back(1)