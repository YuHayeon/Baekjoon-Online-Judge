# 11-3 문자열 뒤집기

import sys

a = list(sys.stdin.readline().rstrip())
end = len(a)
count = 0

for i in range(end-1):
    if a[i] != a[i+1]:
        count += 1

print((count+1)//2)
