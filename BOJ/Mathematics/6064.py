# 6064 : 카잉 달력

import sys

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    mul = (m*n) // gcd(m, n)

    if m < n:
        m, n = n, m
        x, y = y, x

    ans = -1
    for i in range(x-1, mul+1, m):
        if i % n == y-1:
            ans = i+1
            break

    print(ans)