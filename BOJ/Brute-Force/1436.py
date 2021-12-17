# 1436 : 영화감독 숌

import sys

n = int(sys.stdin.readline())
ans = 666
i = 1

while True:
    if i == n:
        break
    ans += 1
    if '666' in str(ans):
        i += 1

print(ans)
