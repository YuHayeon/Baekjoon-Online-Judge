# 11-1 모험가 길드

import sys

n = int(sys.stdin.readline())
rate = list(map(int, sys.stdin.readline().split()))

count = 0
while rate:
    a = max(rate)
    rate.remove(a)
    for _ in range(a-1):
        rate.remove(min(rate))
    count += 1
    if rate ==[] or len(rate)<max(rate) :
        break;

print(count)