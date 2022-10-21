# 1105 : 팔

import sys
input = sys.stdin.readline

l, r = map(str, input().split())
answer = 0
if len(l) != len(r):
    answer = 0
else:
    for i in range(len(l)):
        if int(l[i]) == 8 and int(r[i]) == 8:
            answer += 1
        elif abs(int(l[i])-int(r[i])) > 0:
            break

print(answer)
