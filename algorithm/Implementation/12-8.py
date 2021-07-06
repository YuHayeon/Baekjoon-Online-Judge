# 12-8 : 문자열 재정렬

import sys
s = sys.stdin.readline().rstrip()
s = sorted(s)

sum = 0
while True:
    if s[0].isnumeric() == True:
        sum += int(s[0])
        s.remove(s[0])
    else:
        break

for i in s:
    print(i, end='')
print(sum)