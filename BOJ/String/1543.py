# 1543 : 문서 검색

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
len2 = len(s2)
cnt = 0

while len(s1) > 0:
    find = s1[0:len2]

    if find == s2:
        cnt += 1
        s1 = s1[len2:]
    else:
        s1 = s1[1:]

print(cnt)