# 1475 : 방 번호

import sys

n = list(map(int, sys.stdin.readline().rstrip()))
cnt = [0 for _ in range(10)]
six_and_nine = 0

for i in n:
    if i == 6 or i == 9:
        six_and_nine += 1
    else:
        cnt[i] += 1
max_count = max(cnt)

if six_and_nine % 2 == 1:
    six_and_nine = six_and_nine // 2 + 1
else:
    six_and_nine //= 2

if max_count >= six_and_nine:
    res = max_count
else:
    res = six_and_nine

print(res)
