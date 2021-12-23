# 5555 : 반지

import sys

find = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    string = sys.stdin.readline().rstrip()
    if find[0] not in string:
        continue
    else:
        for i in range(10):
            if find[0] == string[i]:
                string = string[i:]+string[:i]
                break
        if find in string:
            cnt += 1

print(cnt)
