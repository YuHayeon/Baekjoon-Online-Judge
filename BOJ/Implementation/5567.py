# 5567 : 결혼식

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
wedding = []
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in friends[1]:
    wedding.append(i)
    for j in friends[i]:
        wedding.append(j)

wedding = set(wedding)
result = len(wedding)

if result == 0:
    print(0)
else:
    print(result-1)