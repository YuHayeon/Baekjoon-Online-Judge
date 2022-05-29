# 12904 : A와 B

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
result = 0

while True:
    if t == s:
        result = 1
        break

    if t == '':
        break

    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

print(result)