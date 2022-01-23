# 1748 : 수 이어 쓰기 1

import sys
num = int(sys.stdin.readline())
l = len(str(num))
res = 0

for i in range(1, l):
    res += i * 9 * pow(10, (i-1))
res += (num - pow(10, l-1)+1) * l

print(res)