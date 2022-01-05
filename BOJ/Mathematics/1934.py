# 1934 : 최소공배수

import sys

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    mul = (a*b) // gcd(a, b)
    print(mul)
