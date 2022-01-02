# 1110 : 더하기 사이클

import sys
n = str(sys.stdin.readline().rstrip())
if len(n) == 1:
    n = '0'+n[0]
fitst_n = n
cnt = 0

while True:
    new_n = str(int(n[0])+int(n[1]))
    if len(new_n) == 1:
        new_n = '0'+new_n[0]
    n = n[1] + new_n[1]

    cnt += 1
    if fitst_n == str(n):
        break
    
print(cnt)
