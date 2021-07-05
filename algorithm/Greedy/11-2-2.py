# 11-2 : 곱하기 혹은 더하기

import sys
a = list(sys.stdin.readline().rstrip())

result = int(a[0])

for i in range(1, len(a)):
    a[i] = max(int(a[i-1])+int(a[i]), int(a[i-1])*int(a[i]))

print(a[len(a)-1])