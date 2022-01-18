# 15657 : N과 M (8)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
s = []

num.sort()


def back(start):
    if len(s) == m:
        print(' '.join(map(str, s)))

    for i in range(start, n):
        if len(s) == m:
            continue
        s.append(num[i])
        back(i)
        s.pop()


back(0)