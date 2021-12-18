# 15650 : N과 M (2)

import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def back(start):
    if len(s) == m:
        print(' '.join(map(str, s)))

    for i in range(start, n+1):
        if i in s:
            continue
        s.append(i)
        back(i+1)
        s.pop()

back(1)
