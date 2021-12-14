# 1629 : 곱셈

import sys

a, b, c = map(int, sys.stdin.readline().split())
ans = 1


def mul(a, b, mod):
    global ans
    if b % 2 == 1:
        ans = ans * a % mod
    a = a * a % mod
    if b != 1:
        b = b // 2
        return mul(a, b, mod)


mul(a, b, c)

print(ans)
