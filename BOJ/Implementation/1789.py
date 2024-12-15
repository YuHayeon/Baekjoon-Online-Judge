# 1789 : 수들의 합

import sys

s = int(sys.stdin.readline())
total = 0
n = 0

while total <= s:
    n += 1
    total += n
n -= 1

print(n)
