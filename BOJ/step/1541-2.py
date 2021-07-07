# 1541 : 잃어버린 괄호

import sys
s = sys.stdin.readline().split("-")
result = 0
for i in range(len(s)):
    s[i] = sum(map(int, s[i].split("+")))
    result -= s[i]
print(result + 2*(s[0]))