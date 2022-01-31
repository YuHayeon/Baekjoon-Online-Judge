# 2607 : 비슷한 단어

import sys
input = sys.stdin.readline

N = int(input())
string = []
cnt = 0

for _ in range(N):
    string.append(input().strip())

s1 = string[0]
l = len(s1)

for i in range(1, N):
    s2 = list(string[i])

    if len(s2) == l-1:
        for s in s1:
            if s in s2:
                s2.remove(s)
        if len(s2) == 0:
            cnt += 1

    if l <= len(s2) <= l+1:
        for s in s1:
            if s in s2:
                s2.remove(s)
        if len(s2) == 0 or len(s2) == 1:
            cnt += 1

print(cnt)
