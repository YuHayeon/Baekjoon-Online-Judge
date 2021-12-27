# 15650 : N과 M (2)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []

def back(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(start, n+1):
        if i in s:
            continue
        s.append(i)
        back(i)
        s.pop()

back(1)