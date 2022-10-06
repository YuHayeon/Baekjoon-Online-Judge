# 11727 : 2xn 타일링 2

import sys
input = sys.stdin.readline

n = int(input())
d = [0, 1] + [0] * n

for i in range(2, n+1, 2):
    d[i] = d[i-1] * 2 + 1
    d[i+1] = d[i] * 2 - 1

answer = d[n] % 10007
print(answer)
