# 13164 : 행복 유치원

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
children = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(children[i]-children[i-1])

diff.sort()

print(sum(diff[:n-k]))
