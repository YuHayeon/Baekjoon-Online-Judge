# 15654 : N과 M (5)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []


def back():
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in num:
        if i in s:
            continue
        s.append(i)
        back()
        s.pop()


back()
