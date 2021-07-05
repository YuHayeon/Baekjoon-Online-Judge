# 11-5 볼링공 고르기

import sys

n, m = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

k_set = set(k)

result = int(((n * (n-1))/2) - (len(k)-len(k_set)))

print(result)