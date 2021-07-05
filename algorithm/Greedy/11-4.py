# 11-4 만들 수 없는 금액
import sys

n = int(sys.stdin.readline().rstrip())
coin = list(map(int, sys.stdin.readline().split()))

target = 1

coin.sort()
for i in coin:
    if i <= target:
        target += i
    else:
        break

print(target)