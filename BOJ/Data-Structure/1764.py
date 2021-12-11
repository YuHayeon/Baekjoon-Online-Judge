# 1764 : 듣보잡

import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}
ans = []
for i in range(n):
    push = sys.stdin.readline().rstrip()
    dict[push] = push

for _ in range(m):
    find = sys.stdin.readline().rstrip()
    if dict.get(find)==find:
        ans.append(find)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
