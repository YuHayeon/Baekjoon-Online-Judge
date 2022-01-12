# 1292 : 쉽게 푸는 문제

import sys
a, b = map(int, sys.stdin.readline().split())
i, d = 0, 0
result = 0

while True:
    if d >= a:
        result = (d-a+1) * i
        break
    i += 1
    d += i

while True:
    if d >= b:
        result -= (d-b) * i
        break
    i += 1
    d += i
    result += i*i

print(result)