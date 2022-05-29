# 2002 : 추월

import sys
input = sys.stdin.readline

N = int(input())
_in = {}
_out = []
result = 0

for i in range(N):
    _in[input().strip()] = i

for i in range(N):
    _out.append(input().strip())

for i in range(N-1):
    for j in range(i+1, N):
        if _in[_out[i]] > _in[_out[j]]:
            result += 1
            break

print(result)