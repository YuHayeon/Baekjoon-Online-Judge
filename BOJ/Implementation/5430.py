# 5430 : AC

import sys
from collections import deque
input = sys.stdin.readline


def AC(p, x):
    d = 'l'
    q = deque()

    for s in x:
        q.append(s)

    for i in p:
        if i == 'R':
            if d == 'l':
                d = 'r'
            else:
                d = 'l'

        elif i == 'D':
            if q == deque([]):
                return 'error'
            elif d == 'l':
                q.popleft()
            elif d == 'r':
                q.pop()

    if d == 'r':
        q.reverse()

    return '['+','.join(map(str, q))+']'


t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())

    x = input()
    x = x[1:-2]

    if x:
        x = list(map(int, x.split(',')))

    res = AC(p, x)

    print(res)