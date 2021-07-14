# 14-24 : 안테나
# BOJ 18310 : 안테나

import sys

n = int(sys.stdin.readline().rstrip())
home = list(map(int, sys.stdin.readline().split()))

home.sort()
if n%2 == 0:
    ans = home[n//2-1]
else:
    ans = home[n//2]

print(ans)