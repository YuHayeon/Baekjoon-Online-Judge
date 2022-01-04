# 1213 : 팰린드롬 만들기

import sys
s = list(sys.stdin.readline().rstrip())
len_s = len(s)
result = [False for _ in range(len_s)]
s.sort()
i, j, cnt = 1, 0, 0

while j < len_s//2:
    if len(s)==2 and s[0]!=s[1]:
        break
    if s[i-1] == s[i]:
        result[j], result[len_s-j-1] = s[i-1], s[i]
        j += 1
        del s[i-1:i+1]
    else:
        cnt += 1
        i += 1
        if cnt > 1:
            break


if s == []:
    for a in result:
        print(a,end='')
elif len(s) == 1 and len_s % 2 == 1:
    result[len_s//2] = s[0]
    for a in result:
        print(a,end='')
else:
    print("I'm Sorry Hansoo")