# 5582 : 공통 부분 문자열

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s1_len = len(s1)
s2_len = len(s2)
d = [[0 for _ in range(s2_len+1)] for _ in range(s1_len+1)]
answer = 0

for i in range(1, s1_len+1):
    for j in range(1, s2_len+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        answer = max(d[i][j], answer)

print(answer)