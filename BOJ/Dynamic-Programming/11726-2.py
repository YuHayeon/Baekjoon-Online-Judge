# 11726 : 2×n 타일링

import sys
input = sys.stdin.readline

n = int(input())
d = [0, 1, 2]
answer = 1

if n > 1:
    for _ in range(n-2):
        d[0] = d[1]
        d[1] = d[2]
        d[2] = d[0] + d[1]

    answer = d[2] % 10007

print(answer)
